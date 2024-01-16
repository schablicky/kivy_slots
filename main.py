# main.py
from kivy.app import App
from slotmachine import SlotMachineLayout

class SlotMachineApp(App):
    def build(self):
        return SlotMachineLayout()

if __name__ == '__main__':
    SlotMachineApp().run()
