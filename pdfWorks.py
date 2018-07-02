from tkinter import Frame, Button, Tk
from tkinter.ttk import Notebook, Frame
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

        filename = asksaveasfilename(**self.save_options)
        if filename:
            self.converter.convert(filename)

    def __init__(self, master=None):

        Frame.__init__(self, master)
        self.grid()
        self.files_list = None
        self.columnconfigure(0, weight=1)
        self.loadButton = Button(self, text="Выбрать файлы", command=self.show_load_dialog)
        self.loadButton.grid(sticky="we")
        self.convertButton = Button(self, text="Конвертировать", command=self.show_save_dialog, state='disabled')
        self.convertButton.grid(sticky="we")

        self.converter = Converter()
        self.save_options = dict(defaultextension='.pdf',
                                 filetypes=[('PDF file', '*.pdf'), ('All files', '*.*')])
        # TODO add open_options


if __name__ == "__main__":

    root = Tk()
    root.iconbitmap(r'assets\favicon.ico')
    root.title("PDF Works")
    rows = 0
    root.columnconfigure(rows, weight=1)
    root.rowconfigure(rows, weight=1)

    notebook = Notebook(width=230)
    notebook.grid(sticky='NEWS')

    pdfworks = PdfWorks()
    notebook.add(pdfworks, text='Склеить')

    root.mainloop()
    # TODO: разделение pdf на разные страницы
    # TODO: несколько вкладок (по функциям)
