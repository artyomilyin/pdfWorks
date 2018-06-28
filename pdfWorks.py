import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.factory import Factory
from kivy.config import Config
import os

from Converter import Converter


kivy.require('1.10.0')


Config.set('input', 'mouse', 'mouse,disable_multitouch')


class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)


class SaveDialog(FloatLayout):
    save = ObjectProperty(None)
    cancel = ObjectProperty(None)


class MainScreen(GridLayout):

    converter = Converter()

    def dismiss_popup(self):
        self._popup.dismiss()

    def show_load(self):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Выбрать файлы", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def show_save(self):
        content = SaveDialog(save=self.save, cancel=self.dismiss_popup)
        self._popup = Popup(title="Сохранить файл", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def load(self, path, filename):
        with open(os.path.join(path, filename[0])) as stream:
            self.text_input.text = stream.read()

        self.dismiss_popup()

    def save(self, path, filename):
        with open(os.path.join(path, filename), 'w') as stream:
            stream.write(self.text_input.text)

        self.dismiss_popup()

    def update(self, dt):
        pass

    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.cols = 1


class PdfWorksApp(App):
    pass


Factory.register('MainScreen', cls=MainScreen)
Factory.register('LoadDialog', cls=LoadDialog)
Factory.register('SaveDialog', cls=SaveDialog)


if __name__ == '__main__':
    PdfWorksApp().run()