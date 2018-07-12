from tkinter import Tk
from tkinter.ttk import Notebook

from frames import PickAndConvertFrame, PickAndSplitFrame


if __name__ == "__main__":

    rows = 0

    root = Tk()
    root.iconbitmap(r'assets\favicon.ico')
    root.title("PDF Works")
    root.columnconfigure(rows, weight=1)
    root.rowconfigure(rows, weight=1)
    root.resizable(False, False)

    notebook = Notebook(width=230)
    notebook.grid(sticky='NEWS')

    pick_and_convert_frame = PickAndConvertFrame()
    notebook.add(pick_and_convert_frame, text='Склеить')

    pick_and_split_frame = PickAndSplitFrame()
    notebook.add(pick_and_split_frame, text='Разделить')

    root.mainloop()
    # TODO: разделение pdf на разные страницы
    # TODO: несколько вкладок (по функциям)
    # TODO: drag'n'drop feature
