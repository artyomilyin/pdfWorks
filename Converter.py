from PyPDF2 import PdfFileMerger
import img2pdf
import os
import shutil
from datetime import datetime


class Converter:

    SUPPORTED_IMAGE_FILE_FORMATS = ['.jpg', '.png']

    def files_chosen(self):
        if self.input_files is not None:
            return True
        else:
            return False

    def set_input_files(self, files_list):
        print("came to set_input_files():", files_list)

        if not os.path.exists('temp'):
            os.makedirs('temp')

        for file in files_list:
            if file.endswith(tuple(self.SUPPORTED_IMAGE_FILE_FORMATS)):
                new_filename = os.path.join("temp", file+'.pdf')
                with open(os.path.join("INPUT", file), 'rb') as r, open(new_filename, 'wb') as w:
                    try:
                        w.write(img2pdf.convert(r, layout_fun=self.layout_fun))
                    except TypeError as e:
                        print(e)
                self.FINAL_LIST.append(new_filename)

            if file.endswith('.pdf'):
                self.FINAL_LIST.append(os.path.join("input", file))

    def convert(self, filename):

        print("filename to save:", filename)

        merger = PdfFileMerger()

        for file in self.FINAL_LIST:
            self.FILE_HANDLES.append(open(file, 'rb'))
            merger.append(self.FILE_HANDLES[-1])

        with open(filename, 'wb') as w:
            merger.write(w)

        for handle in self.FILE_HANDLES:
            handle.close()

        shutil.rmtree('temp', ignore_errors=True)

    def __init__(self):
        self.input_files = None
        self.a4inpt = (img2pdf.mm_to_pt(210), img2pdf.mm_to_pt(297))
        self.layout_fun = img2pdf.get_layout_fun(self.a4inpt)
        self.FILE_HANDLES = []
        self.FINAL_LIST = []
        self.INPUT_LIST = []


if __name__ == '__main__':
    Converter().convert('OUTPUT/'+datetime.strftime(datetime.now(), '%Y%B%d_%H%M%S')+'.pdf')

