from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.properties import NumericProperty
from kivy.properties import BooleanProperty
from kivy.properties import ObjectProperty
from kivy.clock import Clock


class MainScreen(MDScreen):
    total_seconds: NumericProperty = NumericProperty(0)
    in_timer: BooleanProperty = BooleanProperty(False)
    event: ObjectProperty = ObjectProperty(None, allownone=True)

    def button_text(self) -> str:
        """
        finds the state of the button

        :return: the text displayed depending on the state of the button
        """
        # FIXME: Get to update
        if self.in_timer:
            if self.total_seconds <= 0:
                return "End Timer"
            return "Give Up"
        return "Start Timer"

    def on_button_press(self) -> None:
        """
        an event calls this function

        :return: None
        """

        text = self.button_text()
        if text == "End Timer":
            self.in_timer = False
            if self.event:
                self.event.cancel()
        elif text == "Give Up":
            self.in_timer = False
            if self.event:
                self.event.cancel()
        elif text == "Start Timer":
            self.total_seconds = int(self.ids.slider.value) * 60
            self.in_timer = True
            self.ids.timer_label.text = self.format_time()
            if self.event:
                self.event.cancel()
            self.event = Clock.schedule_interval(self.tick, 1)

    def tick(self, dt: float) -> bool:
        """
        what happens in a tick called by the Clock event

        :param dt: the delta time
        :return: a bool just to stop the event
        """
        if not self.in_timer:
            return False
        self.total_seconds -= 1
        self.ids.timer_label.text = self.format_time()
        if self.total_seconds <= 0:
            self.in_timer = False
            return False
        return True

    def format_time(self) -> str:
        """
        formats seconds into HH:MM:SS

        :return: HH:MM:SS
        """
        hour = self.total_seconds // 3600
        minutes = (self.total_seconds % 3600) // 60
        seconds = self.total_seconds % 60
        return f"{hour:02d}:{minutes:02d}:{seconds:02d}"


class FlowquariumApp(MDApp):
    def build(self) -> None:
        self.theme_cls.primary_palette = "Blue"
        return MainScreen()


if __name__ == "__main__":
    FlowquariumApp().run()
