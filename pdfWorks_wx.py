import wx
from pdfworks_lib.pdfworks import Converter


class ConvertAndMergeTab(wx.Panel):

    def pick_files(self, event):

        with wx.FileDialog(self, "Open XYZ file", wildcard=self.load_options,
                           style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST | wx.FD_MULTIPLE) as fileDialog:
            if fileDialog.ShowModal() != wx.ID_CANCEL:
                self.files_list = fileDialog.GetPaths()
                self.convert_and_merge_button.Enable()
                self.status_bar.SetStatusText("Файлов выбрано: " + str(len(self.files_list)) + ". Можно клеить.")
            print(self.files_list)

    def __init__(self, parent, converter, status_bar):
        wx.Panel.__init__(self, parent)

        self.converter = converter
        self.status_bar = status_bar
        self.image_formats = ';'.join(['*' + x for x in self.converter.SUPPORTED_IMAGE_FILE_FORMATS])
        self.pdf_and_image_formats = ';'.join([self.image_formats] + ['*.pdf'])
        self.load_options = "PDF and IMAGE files (" + self.pdf_and_image_formats + ")|" + self.pdf_and_image_formats\
                            + "|PDF files |*.pdf"\
                            + "|IMAGE files (" + self.image_formats + ")|" + self.image_formats\
                            + "|All files |*.*"
        self.files_list = None

        sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(sizer)

        self.select_files_button = wx.Button(self, label="Выбрать файлы", size=wx.Size(wx.EXPAND, -1))
        self.select_files_button.Bind(wx.EVT_BUTTON, self.pick_files)
        sizer.Add(self.select_files_button)

        self.convert_and_merge_button = wx.Button(self, label="Склеить", size=wx.Size(wx.EXPAND, -1))
        self.convert_and_merge_button.Disable()
        sizer.Add(self.convert_and_merge_button)


class SplitTab(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        t = wx.StaticText(self, -1, "This is the second tab", (20, 20))


class MainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title="pdfWorks",
                          style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER ^ wx.MAXIMIZE_BOX)
        self.SetIcon(wx.Icon('assets/favicon.ico'))
        self.converter = Converter()

        panel = wx.Panel(self)
        notebook = wx.Notebook(panel, size=wx.Size(250, -1))

        self.status_bar = self.CreateStatusBar(1)
        self.status_bar.SetStatusText('Выберите или перенесите в окно файлы')

        convert_and_merge_tab = ConvertAndMergeTab(notebook, self.converter, self.status_bar)
        split_tab = SplitTab(notebook)

        notebook.AddPage(convert_and_merge_tab, "Склеить")
        notebook.AddPage(split_tab, "Разделить")

        sizer = wx.BoxSizer()
        panel.SetSizer(sizer)
        sizer.Add(notebook)
        sizer.SetSizeHints(self)


if __name__ == "__main__":
    app = wx.App()
    MainFrame().Show()
    app.MainLoop()