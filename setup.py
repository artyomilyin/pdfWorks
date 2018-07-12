from cx_Freeze import setup, Executable

base = None

executables = [Executable("pdfWorks.py", base=base)]

packages = ["PyPDF2", "img2pdf", "os", "shutil", "datetime"]
options = {
    'build_exe': {
        'packages':packages,
        #  'include_files':['INPUT/', 'OUTPUT/'],
    },
}

setup(
    name="pdfWorks",
    options=options,
    version="0.1.2",
    description='',
    executables=executables
)