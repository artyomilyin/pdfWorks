from cx_Freeze import setup, Executable

base = None

executables = [Executable("converter.py", base=base)]

packages = ["idna", "PyPDF2", "img2pdf", "os", "shutil", "datetime"]
options = {
    'build_exe': {
        'packages':packages,
        'include_files':['INPUT/', 'OUTPUT/'],
    },
}

setup(
    name = "MergeToPDF",
    options = options,
    version = "0.1.1",
    description = 'Эта программа поможет Вам соединить все ваши изображения и pdf файлы в один большой.\n\
                  Просто положите все нужные файлы в папку Input, запустите converter.exe и заберите готовый файл в папке Output.',
    executables = executables
)