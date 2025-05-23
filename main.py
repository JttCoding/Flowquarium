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
