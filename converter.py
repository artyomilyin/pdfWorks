from PyPDF2 import PdfFileMerger
import img2pdf
import os, shutil
from datetime import datetime


class Converter:

    SUPPORTED_IMAGE_FILE_FORMATS = ['.jpg', '.png']
    a4inpt = (img2pdf.mm_to_pt(210), img2pdf.mm_to_pt(297))
    layout_fun = img2pdf.get_layout_fun(a4inpt)

    INPUT_LIST = []
    FINAL_LIST = []
    FILE_HANDLES = []

    def convert(self, layout_fun=layout_fun):

        if not os.path.exists('temp'):
            os.makedirs('temp')

        for file in os.listdir("INPUT"):
            if file.lower().endswith(tuple(self.SUPPORTED_IMAGE_FILE_FORMATS+['.pdf'])):
                self.INPUT_LIST.append(file.lower())

        for file in self.INPUT_LIST:
            if file.endswith(tuple(self.SUPPORTED_IMAGE_FILE_FORMATS)):
                new_filename = os.path.join("temp", file+'.pdf')
                with open(os.path.join("INPUT", file), 'rb') as r, open(new_filename, 'wb') as w:
                    try:
                        w.write(img2pdf.convert(r, layout_fun=layout_fun))
                    except TypeError as e:
                        print(e)
                self.FINAL_LIST.append(new_filename)

            if file.endswith('.pdf'):
                self.FINAL_LIST.append(os.path.join("input", file))

        merger = PdfFileMerger()

        for file in self.FINAL_LIST:
            self.FILE_HANDLES.append(open(file, 'rb'))
            merger.append(self.FILE_HANDLES[-1])

        with open('OUTPUT/'+datetime.strftime(datetime.now(), '%Y%B%d_%H%M%S')+'.pdf', 'wb') as w:
            merger.write(w)

        for handle in self.FILE_HANDLES:
            handle.close()

        shutil.rmtree('temp', ignore_errors=True)


if __name__ == '__main__':
    Converter().convert()

