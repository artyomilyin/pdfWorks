from tkinter import Tk
from tkinter.ttk import Notebook

from frames import PickAndConvertFrame


if __name__ == "__main__":

    root = Tk()
    root.iconbitmap(r'assets\favicon.ico')
    root.title("PDF Works")
    rows = 0
    root.columnconfigure(rows, weight=1)
    root.rowconfigure(rows, weight=1)

    notebook = Notebook(width=230)
    notebook.grid(sticky='NEWS')

    pick_and_convert_frame = PickAndConvertFrame()
    notebook.add(pick_and_convert_frame, text='Склеить')

    root.mainloop()
    # TODO: разделение pdf на разные страницы
    # TODO: несколько вкладок (по функциям)
