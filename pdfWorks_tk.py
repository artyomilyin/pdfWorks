from tkinter import Frame, Button, Tk
from tkinter.filedialog import askopenfilenames, asksaveasfilename

from Converter import Converter


class PdfWorks(Frame):

    def show_load_dialog(self):

        # TODO set datatypes supported (from Converter class)
        files_list = askopenfilenames()
        self.converter.set_input_files(files_list)

    def show_save_dialog(self):

        # TODO check if dialog was just closed

        filename = asksaveasfilename(**self.save_options)
        self.converter.convert(filename)

    def __init__(self, master=None):

        Frame.__init__(self, master)
        self.grid()
        self.loadButton = Button(master, text="Выбрать файлы", command=self.show_load_dialog)
        self.loadButton.grid()
        self.convertButton = Button(master, text="Конвертировать", command=self.show_save_dialog)
        self.convertButton.grid()

        self.converter = Converter()
        self.save_options = dict(defaultextension='.pdf',
                                 filetypes=[('PDF file', '*.pdf'), ('All files', '*.*')])
        # TODO add open_options


if __name__ == "__main__":

    Tk().iconbitmap(r'assets\favicon.ico')

    pdfworks = PdfWorks()
    pdfworks.mainloop()