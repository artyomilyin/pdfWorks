from cx_Freeze import setup, Executable
import sys


base = None

if sys.platform == 'win32':
    base = "Win32GUI"

executables = [Executable(
    "pdfWorks.py",
    base=base,
    icon='assets/favicon.ico',
)]
# TODO: опасное ПО при установке
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

packages = ["pdfworks_lib", "wx", "itertools", "PyPDF2", "img2pdf", "os", "shutil", "datetime", "ntpath", "sys"]

options = {
    'build_exe': {
        'packages': packages,
        'include_files': ["assets/"],
    },
    'bdist_msi': {
        'data': {"Shortcut": shortcut},
    },
}

setup(
    name="pdfWorks",
    author="Artyom ILYIN",
    options=options,
    version="0.1.5",
    description='pdfWorks',
    executables=executables
)
