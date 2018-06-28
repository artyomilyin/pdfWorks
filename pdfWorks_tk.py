from tkinter import Frame, Button, Tk
from tkinter.filedialog import askopenfilenames, asksaveasfilename

from converter import Converter

class PdfWorks(Frame):

    def show_load_dialog(self):

        filename = askopenfilenames() # show an "Open" dialog box and return the path to the selected file
        print(filename)

    def show_save_dialog(self):

        filename = asksaveasfilename() # show an "Open" dialog box and return the path to the selected file
        print(filename)

    def __init__(self, master=None):

        Frame.__init__(self, master)
        self.grid()
        self.loadButton = Button(master, text="Выбрать файлы", command=self.show_load_dialog)
        self.loadButton.grid()
        self.convertButton = Button(master, text="Конвертировать", command=self.show_save_dialog)
        self.convertButton.grid()

        self.converter = Converter()


if __name__ == "__main__":

    Tk().iconbitmap(r'assets\favicon.ico')

    pdfworks = PdfWorks()
    pdfworks.mainloop()