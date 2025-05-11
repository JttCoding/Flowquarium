from kivymd.app import MDApp


class FlowquariumApp(MDApp):
    def build(self) -> None:
        self.theme_cls.primary_palette = "Blue"


if __name__ == "__main__":
    FlowquariumApp().run()
