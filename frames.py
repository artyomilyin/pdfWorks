from tkinter.ttk import Frame, Button
from tkinter.filedialog import askopenfilenames, asksaveasfilename, askopenfilename, askdirectory

from pdfworks_lib.pdfworks import Converter


class PickAndConvertFrame(Frame):

    def show_load_dialog(self):

        files_list_temp = askopenfilenames(**self.load_options)
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
        self.convertButton = Button(self, text="Склеить", command=self.show_save_dialog, state='disabled')
        self.convertButton.grid(sticky="we")

        self.converter = Converter()

        self.image_formats = '; '.join(['*' + x for x in self.converter.SUPPORTED_IMAGE_FILE_FORMATS])
        self.pdf_and_image_formats = '; '.join([self.image_formats] + ['*.pdf'])
        self.load_options = dict(
            filetypes=[
                ('PDF and IMAGE files (' + self.pdf_and_image_formats + ')', self.pdf_and_image_formats),
                ('PDF files', '*.pdf'),
                ('IMAGE files (' + self.image_formats + ')', self.image_formats),
                ('All files', '*.*')
            ])
        self.save_options = dict(
            defaultextension='.pdf', # TODO: doesn't work
            filetypes=[('PDF file', '*.pdf'), ('All files', '*.*')]
        )


class PickAndSplitFrame(Frame):

    def show_load_dialog(self):

        # TODO set datatypes supported (from Converter class)
        file_name_temp = askopenfilename(**self.load_options)
        if file_name_temp:
            self.file_name = file_name_temp

        if self.file_name:
            self.splitButton['state'] = 'normal'
            self.converter.set_input_files(self.file_name)
        else:
            self.splitButton['state'] = 'disabled'

    def show_save_dialog(self):

        folder_name = askdirectory()
        if folder_name:
            self.converter.split(self.file_name, folder_name)

    def __init__(self, master=None):

        Frame.__init__(self, master)
        self.grid()
        self.file_name = None
        self.columnconfigure(0, weight=1)
        self.loadButton = Button(self, text="Выбрать файл", command=self.show_load_dialog)
        self.loadButton.grid(sticky="we")
        self.splitButton = Button(self, text="Разделить", command=self.show_save_dialog, state='disabled')
        self.splitButton.grid(sticky="we")

        self.converter = Converter()
        self.load_options = dict(filetypes=[('PDF file', '*.pdf'), ('All files', '*.*')])
