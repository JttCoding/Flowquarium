from kivy.clock import Clock
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.core.window import Window


class MainScreen(MDScreen):
    total_seconds: int = 0
    in_timer: bool = False
    event = None

    def on_button_press(self):
        self.total_seconds = int(self.ids.slider.value) * 60
        in_timer = True
        if self.event:
            self.event.cancel()
        self.event = Clock.schedule_interval(self.tick, 1)

    def tick(self, dt: float):
        if self.total_seconds <= 0:
            self.event.cancel()
            in_timer = False
            return None
        self.total_seconds -= 1
        hours = divmod(self.total_seconds, 3600)[0]
        minutes = divmod(self.total_seconds % 3600, 60)[0]
        seconds = self.total_seconds % 60
        self.ids.timer_label.text = f"{hours:02d}:{minutes:02d}:{seconds:02d}"


class FlowquariumApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        return MainScreen()


if __name__ == "__main__":
    FlowquariumApp().run()

from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivy.core.window import Window


class ResponsiveMDLabel(MDLabel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(on_resize=self.adjust_font_size)
        self.adjust_font_size()

    def adjust_font_size(self, *args):
        # Adjust font size based on window width
        self.font_size = max(Window.width / 30, 12)


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"

        screen = MDScreen()

        label = ResponsiveMDLabel(
            text="window label lol",
            halign="center",
            theme_text_color="Primary",
            pos_hint={"center_x": 0.5, "center_y": 0.5}
        )

        screen.add_widget(label)
        return screen


MainApp().run()