from kivymd.app import MDApp
import timer


class FlowquariumApp(MDApp):
    def build(self) -> None:
        self.theme_cls.primary_palette = "Blue"

    def on_button_press(self):
        pass


if __name__ == "__main__":
    FlowquariumApp().run()
