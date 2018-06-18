import kivy
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.gridlayout import GridLayout
kivy.require('1.10.0')


class MainScreen(GridLayout):

    def update(self, dt):
        pass

    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.cols = 2


class PdfWorksApp(App):

    def build(self):
        main_screen = MainScreen()
        Clock.schedule_interval(main_screen.update, 1.0 / 60.0)
        return main_screen


if __name__ == '__main__':
    PdfWorksApp().run()