# -*- coding: utf-8 -*-

# A simple setup script to create an executable running wxPython. This also
# demonstrates the method for creating a Windows executable that does not have
# an associated console.
#
# wxapp.py is a very simple 'Hello, world' type wxPython application
#
# Run the build process by running the command 'python setup.py build'
#
# If everything works well you should find a subdirectory in the build
# subdirectory that contains the files needed to run the application

import sys
from cx_Freeze import setup, Executable
import os


os.environ['TCL_LIBRARY'] = 'c:/python35/tcl/tcl8.6'
os.environ['TK_LIBRARY'] = 'c:/python35/tcl/tk8.6'

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

executables = [
    Executable('FVRT_FrameStart.py', base=base,targetName = "指静脉识别.exe")
]

includes=['numpy.core._methods', 'numpy.lib.format','scipy.sparse.csgraph._validation',
                                          'scipy.spatial.cKDTree','scipy.ndimage._ni_support','matplotlib.backends.backend_tkagg',
                                          'tkinter','tkinter.filedialog']
include_files=['c:/python35/DLLs/tcl86t.dll', 'c:/python35/DLLs/tk86t.dll','D:/GUI/ahashData.json','D:/GUI/dhashData.json',
               'D:/GUI/phashData.json','D:/GUI/whashData.json','D:/GUI/ImInputData.json','D:/GUI/ImMatchData.json',
               'D:/GUI/ImProcessData.json','D:/GUI/arrow.bmp','D:/GUI/left.bmp','D:/GUI/right.bmp']

setup(name='FVRT',
      version='1.0',
      description='FVRT Image Process & Match',
      author = "南京邮电大学 B15050628 柏明潇",
      executables=executables,
      options={'build_exe': {'includes':includes,'include_files':include_files}

               },
      )

print(dir(setup()))
