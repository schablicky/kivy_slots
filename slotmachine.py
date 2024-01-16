# slotmachine.py
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
import random
from symbol import Symbol

class SlotMachine:
    def __init__(self, symbols):
        self.symbols = symbols
        self.result_label = Label(text="Výsledek: ")
        self.spin_button = Button(text="Zatočit", on_press=self.spin)
        self.rows = 3
        self.cols = 4
        self.wheels = [[Image(source=self.symbols[0].image_path) for _ in range(self.rows)] for _ in range(self.cols)]

    def spin(self, instance):
        # Zastavení symbolů náhodně
        results = [[random.choice(self.symbols) for _ in range(self.rows)] for _ in range(self.cols)]

        # Aktualizace obrazů na válích
        for i in range(self.cols):
            for j in range(self.rows):
                self.wheels[i][j].source = results[i][j].image_path

        # Vyhodnocení výsledku
        self.evaluate_results(results)

    def evaluate_results(self, results):
        # Vyhodnocení výsledku podle výherních linií
        for i in range(self.cols - 2):
            for j in range(self.rows - 2):
                symbol = results[i][j]
                if all(results[i + k][j] == symbol for k in range(3)):
                    self.result_label.text = f"Výhra! Trojité shodné symboly nad sebou, sloupec {i + 1}!"
                    return
                if all(results[i][j + k] == symbol for k in range(3)):
                    self.result_label.text = f"Výhra! Trojité shodné symboly vedle sebe, sloupec {i + 1}!"
                    return
        self.result_label.text = "Zkus to znovu. Žádná výhra tentokrát."

class SlotMachineLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(SlotMachineLayout, self).__init__(**kwargs)
        symbols = [
            Symbol("cherry", "symbol_cherry.png"),
            Symbol("lemon", "symbol_lemon.png"),
            Symbol("orange", "symbol_orange.png"),
            Symbol("plum", "symbol_plum.png"),
            Symbol("bell", "symbol_bell.png"),
            Symbol("bar", "symbol_bar.png"),
            Symbol("seven", "symbol_seven.png")
        ]
        self.slot_machine = SlotMachine(symbols)
        self.add_widget(self.slot_machine.result_label)
        for j in range(self.slot_machine.rows):
            row_layout = BoxLayout()
            for i in range(self.slot_machine.cols):
                row_layout.add_widget(self.slot_machine.wheels[i][j])
            self.add_widget(row_layout)
        self.add_widget(self.slot_machine.spin_button)
