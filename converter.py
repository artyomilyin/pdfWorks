from PyPDF2 import PdfFileMerger
import img2pdf
import os, shutil
from datetime import datetime


SUPPORTED_IMAGE_FILE_FORMATS = ['.jpg', '.png']
a4inpt = (img2pdf.mm_to_pt(210),img2pdf.mm_to_pt(297))
layout_fun = img2pdf.get_layout_fun(a4inpt)


INPUT_LIST = []
FINAL_LIST = []
FILE_HANDLES = []

if not os.path.exists('temp'):
    os.makedirs('temp')

for file in os.listdir("input"):
    if file.lower().endswith(tuple(SUPPORTED_IMAGE_FILE_FORMATS+['.pdf'])):
        INPUT_LIST.append(file.lower())

for file in INPUT_LIST:
    if file.endswith(tuple(SUPPORTED_IMAGE_FILE_FORMATS)):
        new_filename = os.path.join("temp", file+'.pdf')
        with open(os.path.join("input", file), 'rb') as r, open(new_filename, 'wb') as w:
            w.write(img2pdf.convert(r, layout_fun=layout_fun))
        FINAL_LIST.append(new_filename)

    if file.endswith('.pdf'):
        FINAL_LIST.append(os.path.join("input", file))

merger = PdfFileMerger()

for file in FINAL_LIST:
    FILE_HANDLES.append(open(file, 'rb'))
    merger.append(FILE_HANDLES[-1])

with open('output/'+datetime.strftime(datetime.now(), '%Y%B%d_%H%M%S')+'.pdf', 'wb') as w:
    merger.write(w)

for handle in FILE_HANDLES:
    handle.close()

shutil.rmtree('temp', ignore_errors=True)


