from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.properties import NumericProperty
from kivy.properties import StringProperty
from kivy.properties import BooleanProperty
from kivy.properties import ObjectProperty
from kivy.clock import Clock


class TimerScreen(MDScreen):
    total_seconds: NumericProperty = NumericProperty(0)
    button_text: StringProperty = StringProperty("")
    in_timer: BooleanProperty = BooleanProperty(False)
    event: ObjectProperty = ObjectProperty(None, allownone=True)

    def get_button_text(self) -> str:
        """
        Finds the state of the button.

        :return: The text displayed depending on the state of the button.
        """
        # FIXME: Get to update
        if self.in_timer:
            if self.total_seconds <= 0:
                self.button_text = "End Timer"
            else:
                self.button_text = "Give Up"
        else:
            self.button_text = "Start Timer"

    def on_button_press(self) -> None:
        """
        An event calls this function.

        :return: None type.
        """
        text = self.button_text
        if text == "End Timer":
            self.in_timer = False
            if self.event:
                self.event.cancel()
                self.ids.timer_label.text = (f"{(int(self.ids.slider.value) // 60):02d}:"
                                             f"{(int(self.ids.slider.value) % 60):02d}:00")
        elif text == "Give Up":
            self.in_timer = False
            if self.event:
                self.event.cancel()
                self.ids.timer_label.text = (f"{(int(self.ids.slider.value) // 60):02d}:"
                                             f"{(int(self.ids.slider.value) % 60):02d}:00")
        elif text == "Start Timer":
            self.total_seconds = int(self.ids.slider.value) * 60
            self.in_timer = True
            self.ids.timer_label.text = self.format_time()
            if self.event:
                self.event.cancel()
            self.event = Clock.schedule_interval(self.tick, 1)
        self.get_button_text()

    def tick(self, dt: float) -> bool:
        """
        What happens in a tick called by the Clock event.

        :param dt: The delta time.
        :return: A boolean just to stop the event.
        """
        if not self.in_timer:
            return False
        self.total_seconds -= 1
        self.ids.timer_label.text = self.format_time()
        self.get_button_text()
        if self.total_seconds <= 0:
            return False
        return True

    def format_time(self) -> str:
        """
        Formats seconds into HH:MM:SS.

        :return: Formatted time in HH:MM:SS.
        """
        hour = self.total_seconds // 3600
        minutes = (self.total_seconds % 3600) // 60
        seconds = self.total_seconds % 60
        return f"{hour:02d}:{minutes:02d}:{seconds:02d}"

    def on_kv_post(self, base_widget: object) -> None:
        self.get_button_text()


class FlowquariumApp(MDApp):
    def build(self) -> None:
        self.theme_cls.primary_palette = "Blue"
        return TimerScreen()


if __name__ == "__main__":
    FlowquariumApp().run()
