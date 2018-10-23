import wx
import os
import itertools
from pdfworks_lib.pdfworks import Converter


class FileDropTarget(wx.FileDropTarget):

    def __init__(self, window, single=False):
        wx.FileDropTarget.__init__(self)
        self.window = window
        self.single = single

    def OnDropFiles(self, x, y, all_rows_list):
        if self.single:
            files_list = [x for x in all_rows_list if not os.path.isdir(x) and os.path.splitext(x)[1] == '.pdf']
            if files_list:
                if len(files_list) > 1:
                    self.window.status_bar.SetStatusText("Нужно только один файл!")
                    return False
                else:
                    self.window.file_name = files_list[0]
                    self.window.split_button.Enable()
                    self.window.status_bar.SetStatusText("Файл выбран. Можно делить.")
                    return True
            return False
        else:
            files_list = [x for x in all_rows_list if not os.path.isdir(x) and os.path.splitext(x)[1] in itertools.chain(self.window.converter.SUPPORTED_IMAGE_FILE_FORMATS, ['.pdf'])]
            if files_list:
                self.window.files_list = files_list
                self.window.convert_and_merge_button.Enable()
                self.window.status_bar.SetStatusText("Файлов выбрано: %d. Можно клеить." % len(self.window.files_list))
                return True
            return False


class ConvertAndMergeTab(wx.Panel):

    def pick_files(self, event):
        with wx.FileDialog(self, "Выбрать файлы", wildcard=self.load_options,
                           style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST | wx.FD_MULTIPLE) as fileDialog:
            if fileDialog.ShowModal() != wx.ID_CANCEL:
                self.files_list = fileDialog.GetPaths()
                self.convert_and_merge_button.Enable()
                self.status_bar.SetStatusText("Файлов выбрано: %d. Можно клеить." % len(self.files_list))

    def convert_and_merge(self, event):
        with wx.FileDialog(self, "Сохранить", wildcard=self.save_options,
                           style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT) as fileDialog:
            if fileDialog.ShowModal() != wx.ID_CANCEL:
                merge_file = fileDialog.GetPath()
                if merge_file in self.files_list:
                    wx.MessageBox('Выбранный файл является входным. Нужно выбрать другой.',
                                  'Error', wx.OK | wx.ICON_INFORMATION)
                    return
                #self.converter(self.files_list, merge_file)
                self.status_bar.SetStatusText("Работаем...")
                #self.converter.convert(self.files_list, fileDialog.GetPath())
                self.converter.convert(self.files_list, merge_file)
                self.status_bar.SetStatusText("Склеено!")

    def __init__(self, parent, converter, status_bar):

        wx.Panel.__init__(self, parent)

        self.converter = converter
        self.status_bar = status_bar
        self.image_formats = ';'.join(['*' + x for x in self.converter.SUPPORTED_IMAGE_FILE_FORMATS])
        self.pdf_and_image_formats = ';'.join([self.image_formats] + ['*.pdf'])
        self.load_options = str("PDF and IMAGE files (%s)|%s|PDF files |*.pdf|IMAGE files (%s)|%s|All files |*.*"
                                % (self.pdf_and_image_formats, self.pdf_and_image_formats,
                                   self.image_formats, self.image_formats))
        self.save_options = "PDF files |*.pdf"
        self.files_list = None

        self.SetDropTarget(FileDropTarget(self))

        sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(sizer)

        self.select_files_button = wx.Button(self, label="Выбрать файлы", size=wx.Size(wx.EXPAND, -1))
        self.select_files_button.Bind(wx.EVT_BUTTON, self.pick_files)
        sizer.Add(self.select_files_button)

        self.convert_and_merge_button = wx.Button(self, label="Склеить", size=wx.Size(wx.EXPAND, -1))
        self.convert_and_merge_button.Bind(wx.EVT_BUTTON, self.convert_and_merge)
        self.convert_and_merge_button.Disable()
        sizer.Add(self.convert_and_merge_button)


class SplitTab(wx.Panel):

    def pick_file(self, event):
        with wx.FileDialog(self, "Выбрать файлы", wildcard=self.load_options,
                           style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:
            if fileDialog.ShowModal() != wx.ID_CANCEL:
                self.file_name = fileDialog.GetPath()
                self.split_button.Enable()
                self.status_bar.SetStatusText("Файл выбран. Можно делить.")

    def split_file(self, event):
        with wx.DirDialog(self, "Выбрать дирректорию", style=wx.DD_DIR_MUST_EXIST) as directoryDialog:
            if directoryDialog.ShowModal() != wx.ID_CANCEL:
                self.status_bar.SetStatusText("Работаем...")
                self.converter.split_pdf(self.file_name, directoryDialog.GetPath())
                self.status_bar.SetStatusText("Разделено!")

    def __init__(self, parent, converter, status_bar):
        wx.Panel.__init__(self, parent)

        self.converter = converter
        self.status_bar = status_bar
        self.load_options = "PDF files |*.pdf"
        self.file_name = None

        self.SetDropTarget(FileDropTarget(self, single=True))

        sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(sizer)

        self.select_file_button = wx.Button(self, label="Выбрать файл", size=wx.Size(wx.EXPAND, -1))
        self.select_file_button.Bind(wx.EVT_BUTTON, self.pick_file)
        sizer.Add(self.select_file_button)

        self.split_button = wx.Button(self, label="Разделить", size=wx.Size(wx.EXPAND, -1))
        self.split_button.Bind(wx.EVT_BUTTON, self.split_file)
        self.split_button.Disable()
        sizer.Add(self.split_button)


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
        split_tab = SplitTab(notebook, self.converter, self.status_bar)

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