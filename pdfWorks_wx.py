import wx


# Define the tab content as classes:
class ConvertAndMergeTab(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(sizer)

        select_files_button = wx.Button(self, label="Выбрать файлы", size=wx.Size(wx.EXPAND, -1))
        sizer.Add(select_files_button)

        convert_and_merge_button = wx.Button(self, label="Склеить", size=wx.Size(wx.EXPAND, -1))
        convert_and_merge_button.Disable()
        sizer.Add(convert_and_merge_button)



class SplitTab(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        t = wx.StaticText(self, -1, "This is the second tab", (20, 20))


class MainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title="pdfWorks", size=wx.Size(270, -1),
                          style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER ^ wx.MAXIMIZE_BOX)
        self.SetIcon(wx.Icon('assets/favicon.ico'))

        panel = wx.Panel(self)
        notebook = wx.Notebook(panel)

        convert_and_merge_tab = ConvertAndMergeTab(notebook)
        split_tab = SplitTab(notebook)

        notebook.AddPage(convert_and_merge_tab, "Склеить")
        notebook.AddPage(split_tab, "Разделить")

        sizer = wx.BoxSizer()
        sizer.Add(notebook, 1, wx.EXPAND)
        #print(notebook.GetBestSize())

        panel.SetSizer(sizer)
        sizer.Layout()

        self.status_bar = self.CreateStatusBar(1)
        self.status_bar.SetStatusText('Выберите или перенесите в окно файлы')


if __name__ == "__main__":
    app = wx.App()
    MainFrame().Show()
    app.MainLoop()