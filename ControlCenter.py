from kivy.app import App 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label 
from kivy.uix.accordion import Accordion, AccordionItem

class ControlCenter(App):
    def build(self):
        accordion = Accordion()

        lights_section = LightsController().create()
        accordion.add_widget(lights_section)

        return accordion
        
class ControlCenter(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'

        accordion = Accordion()
        lights_section = LightsController().create()
        accordion.add_widget(lights_section)

        self.add_widget(accordion)

class ControlCenterApp(App):
    def build(self):
        return ControlCenter()
    
class LightsController:
    def create(self):
        # item = AccordionItem(title='Light Controller')
        # layout = BoxLayout(orientation= 'vertical', spacing=10, padding= 10)

        # # for level in ['Low', 'Medium', 'High']:
        # #     btn = Button(text=level, size_hint_y=None, height = 40)
        # #     btn.bind(on_press=self.on_light_button)
        # #     layout.add_widget(btn)
        
        # # item.add_widget(layout)
        item = Button(text=level, size_hint_y=None, height = 40)
        btn.bind(on_press=self.on_light_button)
        layout.add_widget(btn)

        return item

if __name__ == "__main__":
    ControlCenterApp().run()