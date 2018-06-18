import kivy
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

from converter import Converter

kivy.require('1.10.0')


class MainScreen(GridLayout):

    converter = Converter()

    def on_event(self):
        print("hey")

    def update(self, dt):
        pass

    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.cols = 2
        btn = Button(text="kek")
        btn.bind(on_press=self.on_event)
        #self.add_widget(btn)


class PdfWorksApp(App):

    def build(self):
        main_screen = MainScreen()
        Clock.schedule_interval(main_screen.update, 1.0 / 60.0)
        return main_screen


if __name__ == '__main__':
    PdfWorksApp().run()