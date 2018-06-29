from tkinter import Frame, Button, Tk
from tkinter.filedialog import askopenfilenames, asksaveasfilename

from Converter import Converter


class PdfWorks(Frame):

    def show_load_dialog(self):

        # TODO set datatypes supported (from Converter class)
        files_list_temp = askopenfilenames()
        if files_list_temp:
            self.files_list = files_list_temp

        if self.files_list:
            self.convertButton['state'] = 'normal'
            self.converter.set_input_files(self.files_list)
            self.loadButton['text'] = "Файлов выбрано: " + str(len(self.files_list))
        else:
            self.convertButton['state'] = 'disabled'
            self.loadButton['text'] = "Выбрать файлы"

    def show_save_dialog(self):

        # TODO check if dialog was just closed

        filename = asksaveasfilename(**self.save_options)
        self.converter.convert(filename)

    def __init__(self, master=None):

        Frame.__init__(self, master)
        self.grid()
        self.files_list = None
        self.loadButton = Button(master, text="Выбрать файлы", command=self.show_load_dialog)
        self.loadButton.grid()
        self.convertButton = Button(master, text="Конвертировать", command=self.show_save_dialog, state='disabled')
        self.convertButton.grid()

        self.converter = Converter()
        self.save_options = dict(defaultextension='.pdf',
                                 filetypes=[('PDF file', '*.pdf'), ('All files', '*.*')])
        # TODO add open_options


if __name__ == "__main__":

    Tk().iconbitmap(r'assets\favicon.ico')

    pdfworks = PdfWorks()
    pdfworks.mainloop()