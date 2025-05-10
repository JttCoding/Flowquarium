from kivy.lang import Builder
from kivymd.app import MDApp

KV = """
#:import colors kivymd.color_definitions.colors

MDScreen:
    md_bg_color: colors[app.theme_cls.primary_palette]["200"]
    MDFillRoundFlatButton:
        text: "Start Timer"
        pos_hint: {"center_x": .5, "center_y": .3}
        md_bg_color: app.theme_cls.primary_color
"""


class FlowquariumApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        return Builder.load_string(KV)


if __name__ == "__main__":
    FlowquariumApp().run()
