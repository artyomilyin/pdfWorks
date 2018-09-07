from tkinter import Tk
from tkinter.ttk import Notebook
import wx
from frames_wx import PickAndConvertFrame, PickAndSplitFrame


class TabOne(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        t = wx.StaticText(self, -1, "This is the first tab", (20, 20))


class TabTwo(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        t = wx.StaticText(self, -1, "This is the second tab", (20, 20))


class MainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title="pdfWorks")
        icon = wx.Icon()
        icon.CopyFromBitmap(wx.Bitmap('assets/favicon.ico', wx.BITMAP_TYPE_ANY))
        self.SetIcon(icon)

        panel = wx.Panel(self)
        notebook = wx.Notebook(panel)

        pick_and_convert_frame = PickAndConvertFrame(notebook)
        pick_and_split_frame = TabTwo(notebook)

        notebook.AddPage(pick_and_convert_frame, "Склеить")
        notebook.AddPage(pick_and_split_frame, "Разделить")

        sizer = wx.BoxSizer()
        sizer.Add(notebook, 1, wx.EXPAND)
        sizer.Layout()
        panel.SetSizer(sizer)


if __name__ == "__main__":

    """rows = 0

    root = Tk()
    
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
"""

    # Define the tab content as classes:


    app = wx.App()
    MainFrame().Show()
    app.MainLoop()


    # TODO: разделение pdf на разные страницы
    # TODO: несколько вкладок (по функциям)
    # TODO: drag'n'drop feature
