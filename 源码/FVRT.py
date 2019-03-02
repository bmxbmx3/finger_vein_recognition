from PIL.Image import open as ImOpen,fromarray,BILINEAR
from numpy import *
from scipy.sparse import *
from scipy.signal import *
from skimage.filters import threshold_niblack
from matplotlib.pyplot import *
import cv2
from skimage import morphology
import imagehash
from MySQLdb.connections import *
import wx

# 建立fvrt数据库中的image表
# CREATE TABLE if NOT EXISTS image ( id int unsigned primary key auto_increment,imname text NOT NULL,imdata longtext NOT NULL,
# imcount INT NOT NULL,KEY(imname(15)))character set = utf8;
# 指静脉图像预处理


class FVRT:

    # 初始化各系数

    # 变换后的宽
    WIDTH = 75

    # 变换后的高
    HEIGHT = 170

    # 灰度放大系数
    THREFACTOR = 4

    # 隶属度分割界限
    THREGRAY = 0.3

    # 迭代次数
    ITER = 3

    # Niblack模板边长
    SIDELENGTH = 11

    # 补偿权值
    THREK = 0.05

    # 开运算模板边长
    OPENSIDE = 3

    # 闭运算模板边长
    CLOSEDSIDE = 3

    # 中值滤波模板边长
    BLURSIDE = 5

    # 圈定面积
    MINSIZE = 20

    # 输入原始图像
    def __init__(self, addr):
        # if addr!='':
        self.__im = ImOpen(addr).convert('L')
        # else:
        #     self.__im=image

    # 尺寸归一化
    def SizeNorm(self, width, height):
        self.__im = self.__im.resize((width, height), BILINEAR)

    # 灰度归一化
    def GrayNorm(self):
        pix = array(self.__im)
        norm = Normalize(vmin=pix.min(), vmax=pix.max())
        pix = norm(pix) * 255
        pix = pix.astype(int32)
        self.__im = fromarray(pix)

    # 基于方向的谷型检测
    def DirectValley(self, ThreFactor):
        pix = array(self.__im)
        row = array([0, 2, 4, 6, 8])
        value = array([3, -1, -4, -1, 3])
        A = {}
        for i in range(4):
            if i == 0:
                col = row
            elif i == 1:
                col = array([2, 3, 4, 5, 6])
            elif i == 2:
                col = array([4, 4, 4, 4, 4])
            else:
                col = array([6, 5, 4, 3, 2])
            A[i] = csc_matrix((value, (row, col)), shape=(9, 9)).toarray()
            A[i + 4] = rot90(A[i])

        pixdict = {}
        for i in range(8):
            pixdict[i] = convolve2d(pix, A[i], 'same')

        m, n = pix.shape
        for x in range(m):
            for y in range(n):
                valmax = -1000
                for i in range(8):
                    if pixdict[i][x, y] >= valmax:
                        valmax = pixdict[i][x, y]
                if valmax >= 0:
                    pix[x, y] = valmax
                else:
                    pix[x, y] = 0

        nozero_num = count_nonzero(pix)
        nozero_avg = sum(pix) / nozero_num

        for x in range(m):
            for y in range(n):
                if pix[x, y] >= (ThreFactor * nozero_avg):
                    pix[x, y] = ThreFactor * nozero_avg
        self.__im = fromarray(pix)

    # 图像模糊增强
    def BlurEnhance(self, ThreGray, Iter):
        pix = array(self.__im)
        pix = sin(pix * pi / (2 * 255))
        for i in arange(Iter):
            pix = (sin(pi * (pix - ThreGray)) + 1) / 2
        pix = 255 * arcsin(pix ** sqrt(Iter)) * 2 / pi
        self.__im = fromarray(pix)

    # 图像阈值分割
    def ThreSegment(self, SideLength, ThreK):
        pix = array(self.__im)
        thresh_pix = threshold_niblack(pix, window_size=SideLength * SideLength, k=ThreK)
        binary_pix = pix > thresh_pix
        pix = binary_pix.astype(int) * 255
        self.__im = fromarray(pix)

    # 图像去噪
    def Denoise(self, OpenSide, ClosedSide, BlurSide):
        im = self.__im
        im = cv2.cvtColor(asarray(im).astype(uint8), cv2.COLOR_GRAY2BGR)
        openkernel = cv2.getStructuringElement(cv2.MORPH_RECT, (OpenSide, OpenSide))
        opening = cv2.morphologyEx(array(im), cv2.MORPH_OPEN, openkernel)
        closedkernel = cv2.getStructuringElement(cv2.MORPH_RECT, (ClosedSide, ClosedSide))
        closed = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, closedkernel)
        result = cv2.medianBlur(closed, BlurSide)
        pix = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
        self.__im = fromarray(pix)

    # 图像细化
    def Thin(self):
        pix = array(self.__im)
        pix = pix / 255
        pix = morphology.skeletonize(pix)
        pix = pix.astype(int) * 255
        self.__im = fromarray(pix)

    # 二值化图像去除残余斑点
    def CleanSmallObject(self, MinSize):
        pix = array(self.__im) / 255
        pix = pix.astype(bool)
        pix = morphology.remove_small_objects(pix, min_size=MinSize, connectivity=2)
        pix = pix.astype(int) * 255
        self.__im = fromarray(pix)

    # 获得图像数组
    def GetArray(self):
        return array(self.__im)

    # 获得图像
    def GetImage(self):
        return self.__im

    # 显示图像
    def ShowImage(self):
        self.__im.show()

    # 设置各系数
    @staticmethod
    def SetFactor(width=75, height=170, ThreFactor=4, ThreGray=0.3, Iter=3, SideLength=11, ThreK=0.05, OpenSide=3, ClosedSide=3, BlurSide=5, MinSize=20):
        FVRT.WIDTH = width
        FVRT.HEIGHT = height
        FVRT.THREFACTOR = ThreFactor
        FVRT.THREGRAY = ThreGray
        FVRT.ITER = Iter
        FVRT.SIDELENGTH = SideLength
        FVRT.THREK = ThreK
        FVRT.OPENSIDE = OpenSide
        FVRT.CLOSEDSIDE = ClosedSide
        FVRT.BLURSIDE = BlurSide
        FVRT.MINSIZE = MinSize

    # 一键操作图像
    @staticmethod
    def OneKey(addr):
        image = FVRT(addr)
        image.SizeNorm(FVRT.WIDTH,FVRT.HEIGHT)
        image.GrayNorm()
        image.DirectValley(FVRT.THREFACTOR)
        image.BlurEnhance(FVRT.THREGRAY, FVRT.ITER)
        image.ThreSegment(FVRT.SIDELENGTH, FVRT.THREK)
        image.Denoise(FVRT.OPENSIDE, FVRT.CLOSEDSIDE, FVRT.BLURSIDE)
        image.Thin()
        image.CleanSmallObject(FVRT.MINSIZE)
        return image.GetImage()

# 指静脉图像匹配


class ImReg:

    # 设置相似度阈值
    THRESHOLD = 0.7

    # 载入需要匹配的图像
    def __init__(self, im1, im2):
        self.__im1 = im1
        self.__im2 = im2

    # 感知哈希
    def phash(self, hash_size=8, highfreq_factor=4):
        hash1 = imagehash.phash(self.__im1, hash_size=hash_size, highfreq_factor=highfreq_factor)
        hash2 = imagehash.phash(self.__im2, hash_size=hash_size, highfreq_factor=highfreq_factor)
        similarity = 1 - (hash1 - hash2) / len(hash1.hash)**2
        answer = '是' if similarity >= ImReg.THRESHOLD else '否'
        return similarity, answer

    # 平均散列
    def ahash(self, hash_size=8):
        hash1 = imagehash.average_hash(self.__im1, hash_size=hash_size)
        hash2 = imagehash.average_hash(self.__im2, hash_size=hash_size)
        similarity = 1 - (hash1 - hash2) / len(hash1.hash)**2
        answer = '是' if similarity >= ImReg.THRESHOLD else '否'
        return similarity, answer

    # 梯度散列
    def dhash(self, hash_size=8):
        hash1 = imagehash.dhash(self.__im1, hash_size=hash_size)
        hash2 = imagehash.dhash(self.__im2, hash_size=hash_size)
        similarity = 1 - (hash1 - hash2) / len(hash1.hash)**2
        answer = '是' if similarity >= ImReg.THRESHOLD else '否'
        return similarity, answer

    # 小波散列
    def whash(self, hash_size=8, image_scale=None, mode='haar', remove_max_haar_ll=True):
        hash1 = imagehash.whash(self.__im1, image_scale=image_scale, hash_size=hash_size, mode=mode, remove_max_haar_ll=remove_max_haar_ll)
        hash2 = imagehash.whash(self.__im2, image_scale=image_scale, hash_size=hash_size, mode=mode, remove_max_haar_ll=remove_max_haar_ll)
        similarity = 1 - (hash1 - hash2) / len(hash1.hash)**2
        answer = '是' if similarity >= ImReg.THRESHOLD else '否'
        return similarity, answer

# 指静脉图像数据库的操作


class ImDB:

    # 添加图像到fvrt数据库的image表中
    @staticmethod
    def AddIm(imname, im):
        imdataInt = array(im).tolist()
        imdataStr = ''
        k = 0
        for i in imdataInt:
            k = k + 1
            if k < len(imdataInt):
                imdataStr = imdataStr + ','.join(str(e) for e in i) + '/'
            else:
                imdataStr = imdataStr + ','.join(str(e) for e in i)
        imdataStr = imdataStr.encode(encoding="utf-8")
        conn = Connection(host="localhost", user="root", passwd="123456", charset="utf8")
        cursor = conn.cursor()
        cursor.execute('''USE fvrt;''')
        cursor.execute('''SELECT COUNT(*) FROM image WHERE imname = %s;''', (imname,))
        imcount = cursor.fetchone()[0]
        imcount = imcount + 1
        cursor.execute('''INSERT image(imname,imdata,imcount) VALUES ( %s, %s, %s);''', (imname, imdataStr, imcount))
        conn.commit()
        cursor.close()
        conn.close()

    # 从fvrt数据库的image表中获得图像
    @staticmethod
    def GetIm(id=1, imname='', imcount=1):
        conn = Connection(host="localhost", user="root", passwd="123456", charset="utf8")
        cursor = conn.cursor()
        cursor.execute('''USE fvrt;''')
        if imname == '' and imcount == 1:
            # 从fvrt数据库的image表中获得id指定的不指名图像
            cursor.execute('''SELECT imdata FROM image WHERE id = %s;''', (id,))
        else:
            # 从fvrt数据库的image表中获得某个名称指定的第n个图像
            cursor.execute('''SELECT imdata FROM image WHERE imname = %s AND imcount = %s;''', (imname, imcount))
        imdataStr = cursor.fetchone()[0]
        conn.commit()
        cursor.close()
        conn.close()
        imdataStr=imdataStr.decode("utf-8")
        imdataInt = []
        for i in imdataStr.split('/'):
            imdataSlice = map(lambda x: int(x), i.split(','))
            imdataInt.append(list(imdataSlice))
        return fromarray(asarray(imdataInt))

    # 获得image表中存储的图像总数
    @staticmethod
    def GetImNum():
        conn = Connection(host="localhost", user="root", passwd="123456", charset="utf8")
        cursor = conn.cursor()
        cursor.execute('''USE fvrt;''')
        cursor.execute('''SELECT COUNT(*) FROM image;''')
        imsize = cursor.fetchone()[0]
        conn.commit()
        cursor.close()
        conn.close()
        return imsize

    # 完全清除fvrt数据库的image表中的数据
    @staticmethod
    def DelAll():
        conn = Connection(host="localhost", user="root", passwd="123456", charset="utf8")
        cursor = conn.cursor()
        cursor.execute('USE fvrt;')
        cursor.execute('TRUNCATE image;')
        conn.commit()
        cursor.close()
        conn.close()


if __name__ == '__main__':
    a=ImOpen("D:\\指静脉识别STITP\\指静脉样本\\F0101.bmp")
    b=ImOpen("D:\\指静脉识别STITP\\指静脉样本\\F0201.bmp")
    r=ImReg(a,b)
    r1,r2=ImReg.whash(hash_size=16)
    print(r1,r2)
