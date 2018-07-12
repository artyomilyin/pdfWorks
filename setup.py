from cx_Freeze import setup, Executable
import os
import sys


os.environ['TCL_LIBRARY'] = 'C:/Users/aailyin/AppData/Local/Programs/Python/Python36-32/tcl/tcl8.6'
os.environ['TK_LIBRARY'] = 'C:/Users/aailyin/AppData/Local/Programs/Python/Python36-32/tcl/tk8.6'

base = None

if sys.platform == 'win32':
    base = "Win32GUI"

executables = [Executable(
    "pdfWorks.py",
    base=base,
    icon='assets/favicon.ico',
)]

shortcut = [
    ("DesktopShortcut",         # Shortcut
     "DesktopFolder",           # Directory_
     "pdfWorks",                # Name
     "TARGETDIR",               # Component_
     "[TARGETDIR]pdfWorks.exe", # Target
     None,                      # Arguments
     None,                      # Description
     None,                      # Hotkey
     None,                      # Icon
     None,                      # IconIndex
     None,                      # ShowCmd
     'TARGETDIR'                # WkDir
     )
    ]

packages = ["tkinter", "PyPDF2", "img2pdf", "os", "shutil", "datetime", "ntpath", "sys"]

options = {
    'build_exe': {
        'packages': packages,
        'include_files': ["assets/", "DDLs/tcl86t.dll", "DDLs/tk86t.dll"],
    },
    'bdist_msi': {
        'data': {"Shortcut": shortcut},
    },
}

setup(
    name="pdfWorks",
    options=options,
    version="0.1.2",
    description='',
    executables=executables
)
