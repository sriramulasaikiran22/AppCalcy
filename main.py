import kivy
import json

from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivy.graphics import Ellipse
from kivy.uix.button import Button
from kivy.uix.widget import Widget

Window.clearcolor = (1, 1, 1, 1)


class ColorFrame(Widget):
    pass


class ColorWidget(Widget):
    pass


class CircleButton(Button):
    def __init__(self, **kwargs):
        super(CircleButton, self).__init__(**kwargs)
        with self.canvas:
            Ellipse(pos=self.pos, size=self.size)


class MainWindow(Screen):
    pass


class SWindow(Screen):
    text_box = ObjectProperty(None)
    result = ObjectProperty(None)

    def clear(self):
        self.ids.text_box.text = "0"
        self.ids.res.text = ""

    def press_button(self, button):

        prior = self.ids.text_box.text
        if prior == '0':
            self.ids.text_box.text = ''
        if len(prior) >= 1:
            if button == "(":
                if prior[-1] not in ['+', '-', '/', '%']:
                    self.ids.text_box.text += ('*'+button)
                    return
        self.ids.text_box.text += button

    def evaluate(self):
        self.ids.res.text = ""
        try:
            result = eval(self.ids.text_box.text)
        except Exception as e:
            return
        self.ids.res.text = str(result)

    def undo(self):
        prior = self.ids.text_box.text
        p_string = prior[:-1]
        self.ids.text_box.text = p_string


class TWindow(Screen):

    def clear(self):
        self.ids.text_box_input.text = ""
        self.ids.text_box_output.text = ""

    def press_button(self, button):

        prior = self.ids.text_box_input.text
        if prior == '0':
            self.ids.text_box_input.text = ''
        self.ids.text_box_input.text += button

    def undo(self):
        prior = self.ids.text_box_input.text
        p_string = prior[:-1]
        self.ids.text_box_input.text = p_string

    def update_spinner_values(self):
        area_values = ['Gunta', 'Gajam', 'Cent', 'Square_foot','Acre','Square_meter','Hectare']
        length_values = ['Meter', 'Kilometer', 'Centimeter', 'Millimeter','Inch','Yard','Foot','Mile']
        weight_values = ['Ton', 'Quintal', 'Kilogram', 'Gram', 'Milligram']
        gold_values = ['Gram', 'Kilogram', 'Savaran', 'Tola']

        first_spinner_val = self.ids.spinner_conversion_type.text
        if first_spinner_val == "AreaConversions":
            self.ids.spinner_conversion_input_type.values = area_values
        elif first_spinner_val == "LengthConversions":
            self.ids.spinner_conversion_input_type.values = length_values
        elif first_spinner_val == "WeightConversions":
            self.ids.spinner_conversion_input_type.values = weight_values
        elif first_spinner_val == "GoldConversions":
            self.ids.spinner_conversion_input_type.values = gold_values

    def update_out_spinner_options(self):
        area_values = ['Gunta', 'Gajam', 'Cent', 'Square_foot', 'Acre', 'Square_meter', 'Hectare']
        length_values = ['Meter', 'Kilometer', 'Centimeter', 'Millimeter', 'Inch', 'Yard', 'Foot', 'Mile']
        weight_values = ['Ton', 'Quintal', 'Kilogram', 'Gram', 'Milligram']
        gold_values = ['Gram', 'Kilogram', 'Savaran', 'Tola']

        second_spinner_val = self.ids.spinner_conversion_input_type.text
        if second_spinner_val in area_values:
            self.ids.spinner_conversion_output_type.values = [value for value in area_values if second_spinner_val != value]
        if second_spinner_val in length_values:
            self.ids.spinner_conversion_output_type.values = [value for value in length_values if second_spinner_val != value]
        if second_spinner_val in weight_values:
            self.ids.spinner_conversion_output_type.values = [value for value in weight_values if second_spinner_val != value]
        if second_spinner_val in gold_values:
            self.ids.spinner_conversion_output_type.values = [value for value in gold_values if second_spinner_val != value]

    def get_conversion_result(self):
        first_spinner_val = self.ids.spinner_conversion_type.text
        if first_spinner_val == "AreaConversions":
            self.get_area_conversion_result()
        elif first_spinner_val == "LengthConversions":
            self.get_length_conversion_result()
        elif first_spinner_val == "WeightConversions":
            self.get_weight_conversion_result()
        elif first_spinner_val == "GoldConversions":
            self.get_gold_conversion_result()

    def get_area_conversion_result(self):
        area_types = ['Gunta', 'Gajam', 'Cent', 'Square_foot', 'Acre', 'Square_meter', 'Hectare']
        input_val = self.ids.text_box_input.text
        input_type = self.ids.spinner_conversion_input_type.text
        output_type = self.ids.spinner_conversion_output_type.text
        if input_val.replace('.', '').isdigit():
            if input_type == 'Acre':
                Gunta = float(input_val) / 0.025
                Gajam = float(input_val) * 4840
                Cent = float(input_val) * 100
                Square_foot = float(input_val) * 43560
                Square_meter = float(input_val) * 4047
                Hectare = float(input_val) / 2.471
                areas = ['Gajam', 'Cent', 'Square_foot', 'Square_meter', 'Hectare', 'Gunta']
                val = [Gajam, Cent, Square_foot, Square_meter, Hectare, Gunta]
                results = {area: val for area, val in zip(areas, val)}
                print(results)
                self.ids.text_box_output.text = str(round(results[output_type], 5))
            elif input_type == 'Gunta':
                Gajam = float(input_val) * 121
                Cent = float(input_val) * 2.5
                Square_foot = float(input_val) * 1089
                Acre = float(input_val) * 0.025
                Square_meter = 101.17 * float(input_val)
                Hectare = float(input_val) * 0.010117141056
                areas = ['Gajam', 'Cent', 'Square_foot', 'Square_meter', 'Hectare', 'Acre']
                val = [Gajam, Cent, Square_foot, Square_meter, Hectare, Acre]
                results = {area: val for area, val in zip(areas, val)}
                print(results)
                self.ids.text_box_output.text = str(round(results[output_type], 5))
            elif input_type == 'Gajam':
                Gunta = float(input_val) / 121
                Cent = float(input_val) * 0.020661138759433
                Square_foot = float(input_val) * 9
                Acre = float(input_val) / 4840
                Square_meter = float(input_val) * 0.83612736
                Hectare = float(input_val) * 0.000083612736
                areas = ['Gunta', 'Cent', 'Square_foot', 'Square_meter', 'Hectare', 'Acre']
                val = [Gunta, Cent, Square_foot, Square_meter, Hectare, Acre]
                results = {area: val for area, val in zip(areas, val)}
                print(results)
                self.ids.text_box_output.text = str(round(results[output_type], 5))
            elif input_type == 'Cent':
                Gunta = float(input_val) / 2.5
                Gajam = float(input_val) * 48.4  # also sqyd
                Square_foot = float(input_val) * 435.56
                Acre = float(input_val) / 100
                Square_meter = float(input_val) * 40.47
                Hectare = float(input_val) * 0.004
                areas = ['Gunta', 'Gajam', 'Square_foot', 'Square_meter', 'Hectare', 'Acre']
                val = [Gunta, Gajam, Square_foot, Square_meter, Hectare, Acre]
                results = {area: val for area, val in zip(areas, val)}
                print(results)
                self.ids.text_box_output.text = str(round(results[output_type], 5))
            elif input_type == 'Square_foot':
                Gunta = float(input_val) / 1089
                Gajam = float(input_val) / 9
                Cent = float(input_val) / 435.56
                Acre = float(input_val) / 43560
                Square_meter = float(input_val) / 10.764
                Hectare = float(input_val) / 107639
                areas = ['Gunta', 'Gajam', 'Cent', 'Square_meter', 'Hectare', 'Acre']
                val = [Gunta, Gajam, Cent, Square_meter, Hectare, Acre]
                results = {area: val for area, val in zip(areas, val)}
                print(results)
                self.ids.text_box_output.text = str(round(results[output_type], 5))
            elif input_type == 'Square_meter':
                Gunta = float(input_val) / 101.17
                Gajam = float(input_val) / 0.83612736
                Cent = float(input_val) / 40.47
                Square_foot = float(input_val) * 10.764
                Acre = float(input_val) / 4047
                Hectare = float(input_val) / 10000
                areas = ['Gunta', 'Gajam', 'Cent', 'Square_foot', 'Hectare', 'Acre']
                val = [Gunta, Gajam, Cent, Square_foot, Hectare, Acre]
                results = {area: val for area, val in zip(areas, val)}
                print(results)
                self.ids.text_box_output.text = str(round(results[output_type], 5))
            elif input_type == 'Hectare':
                Gunta = float(input_val) / 0.010117141056
                Gajam = float(input_val) / 0.000083612736
                Cent = float(input_val) / 0.004
                Square_foot = float(input_val) * 107639
                Acre = float(input_val) * 2.471
                Square_meter = float(input_val) * 10000
                areas = ['Gunta', 'Gajam', 'Cent', 'Square_foot', 'Square_meter', 'Acre']
                val = [Gunta, Gajam, Cent, Square_foot, Square_meter, Acre]
                results = {area: val for area, val in zip(areas, val)}
                print(results)
                self.ids.text_box_output.text = str(round(results[output_type], 5))

    def get_length_conversion_result(self):
        length_values = ['Meter', 'Kilometer', 'Centimeter', 'Millimeter', 'Inch', 'Yard', 'Foot', 'Mile']
        input_val = self.ids.text_box_input.text
        input_type = self.ids.spinner_conversion_input_type.text
        output_type = self.ids.spinner_conversion_output_type.text
        if input_val.replace('.', '').isdigit():
            if input_type == 'Kilometer':
                Meter = float(input_val) * 1000
                Centimeter = float(Meter) * 100
                Millimeter = float(Centimeter) * 10
                Inch = float(Centimeter) * 0.39370079
                Yard = float(Meter) * 1.09361
                Foot = float(Meter) * 3.28084
                Mile = float(input_val) / 1.609
                lengths = ['Meter', 'Centimeter', 'Millimeter', 'Inch', 'Yard', 'Foot', 'Mile']
                val = [Meter, Centimeter, Millimeter, Inch, Yard, Foot, Mile]
                results = {area: val for area, val in zip(lengths, val)}
                print(results)
                self.ids.text_box_output.text = str(round(results[output_type], 5))
            elif input_type == 'Meter':
                Kilometer = float(input_val) / 1000
                Centimeter = float(input_val) * 100
                Millimeter = float(input_val) * 10
                Inch = float(input_val) * 39.37
                Yard = float(input_val) * 1.09361
                Foot = float(input_val) * 3.28084
                Mile = float(input_val) / 1609
                lengths = ['Kilometer', 'Centimeter', 'Millimeter', 'Inch', 'Yard', 'Foot', 'Mile']
                val = [Kilometer, Centimeter, Millimeter, Inch, Yard, Foot, Mile]
                results = {area: val for area, val in zip(lengths, val)}
                print(results)
                self.ids.text_box_output.text = str(round(results[output_type], 5))
            elif input_type == 'Centimeter':
                Millimeter = float(input_val) * 10
                Meter = float(input_val) / 100
                Kilometer = float(input_val) / 100000
                Inch = float(input_val) / 2.54
                Yard = float(input_val) / 91.44
                Foot = float(input_val) / 30.48
                Mile = float(input_val) / 160900
                lengths = ['Kilometer', 'Meter', 'Millimeter', 'Inch', 'Yard', 'Foot', 'Mile']
                val = [Kilometer, Meter, Millimeter, Inch, Yard, Foot, Mile]
                results = {area: val for area, val in zip(lengths, val)}
                print(results)
                self.ids.text_box_output.text = str(round(results[output_type], 5))
            elif input_type == 'Millimeter':
                Centimeter = float(input_val) / 10
                Meter = Centimeter / 100
                Kilometer = Meter / 1000
                Inch = Centimeter * 0.39370079
                Yard = Meter * 1.09361
                Foot = Meter * 3.28084
                Mile = Kilometer * 0.621371
                lengths = ['Kilometer', 'Meter', 'Centimeter', 'Inch', 'Yard', 'Foot', 'Mile']
                val = [Kilometer, Meter, Centimeter, Inch, Yard, Foot, Mile]
                results = {area: val for area, val in zip(lengths, val)}
                print(results)
                self.ids.text_box_output.text = str(round(results[output_type], 5))
            elif input_type == 'Inch':
                Centimeter = float(input_val) * 2.54
                Meter = Centimeter / 100
                Kilometer = Meter / 1000
                Millimeter = Centimeter * 10
                Yard = Meter * 1.09361
                Foot = Meter * 3.28084
                Mile = Kilometer * 0.621371
                lengths = ['Kilometer', 'Meter', 'Centimeter', 'Millimeter', 'Yard', 'Foot', 'Mile']
                val = [Kilometer, Meter, Centimeter, Millimeter, Yard, Foot, Mile]
                results = {area: val for area, val in zip(lengths, val)}
                print(results)
                self.ids.text_box_output.text = str(round(results[output_type], 5))
            elif input_type == 'Yard':
                Centimeter = float(input_val) * 91.44
                Meter = Centimeter / 100
                Kilometer = Meter / 1000
                Millimeter = Centimeter * 10
                Inch = Centimeter * 0.39370079
                Foot = Meter * 3.28084
                Mile = Kilometer * 0.621371
                lengths = ['Kilometer', 'Meter', 'Centimeter', 'Millimeter', 'Inch', 'Foot', 'Mile']
                val = [Kilometer, Meter, Centimeter, Millimeter, Inch, Foot, Mile]
                results = {area: val for area, val in zip(lengths, val)}
                print(results)
                self.ids.text_box_output.text = str(round(results[output_type], 5))
            elif input_type == 'Foot':
                Centimeter = float(input_val) * 30.48
                Meter = Centimeter / 100
                Kilometer = Meter / 1000
                Millimeter = Centimeter * 10
                Inch = Centimeter * 0.39370079
                Yard = Meter * 1.09361
                Mile = Kilometer * 0.621371
                lengths = ['Kilometer', 'Meter', 'Centimeter', 'Millimeter', 'Inch', 'Yard', 'Mile']
                val = [Kilometer, Meter, Centimeter, Millimeter, Inch, Yard, Mile]
                results = {area: val for area, val in zip(lengths, val)}
                print(results)
                self.ids.text_box_output.text = str(round(results[output_type], 5))
            elif input_type == 'Mile':
                Centimeter = float(input_val) * 160934.4
                Meter = Centimeter / 100
                Kilometer = Meter / 1000
                Millimeter = Centimeter * 10
                Inch = Centimeter * 0.39370079
                Yard = Meter * 1.09361
                Foot = Meter * 3.28084
                lengths = ['Kilometer', 'Meter', 'Centimeter', 'Millimeter', 'Inch', 'Yard', 'Foot']
                val = [Kilometer, Meter, Centimeter, Millimeter, Inch, Yard, Foot]
                results = {area: val for area, val in zip(lengths, val)}
                print(results)
                self.ids.text_box_output.text = str(round(results[output_type], 5))

    def get_weight_conversion_result(self):
        weight_values = ['Ton', 'Quintal', 'Kilogram', 'Gram', 'Milligram']
        input_val = self.ids.text_box_input.text
        input_type = self.ids.spinner_conversion_input_type.text
        output_type = self.ids.spinner_conversion_output_type.text
        if input_val.replace('.', '').isdigit():
            if input_type == 'Ton':
                Kilogram = float(input_val) * 1000
                Gram = Kilogram / 1000
                Milligram = Gram / 1000
                Quintal = float(input_val) * 10
                weights = ['Quintal', 'Kilogram', 'Gram', 'Milligram']
                val = [Quintal, Kilogram, Gram, Milligram]
                results = {area: val for area, val in zip(weights, val)}
                print(results)
                self.ids.text_box_output.text = str(round(results[output_type], 5))
            elif input_type == 'Quintal':
                Kilogram = float(input_val) * 100
                Gram = Kilogram / 1000
                Milligram = Gram / 1000
                Ton = float(input_val) / 10
                weights = ['Ton', 'Kilogram', 'Gram', 'Milligram']
                val = [Ton, Kilogram, Gram, Milligram]
                results = {area: val for area, val in zip(weights, val)}
                print(results)
                self.ids.text_box_output.text = str(round(results[output_type], 5))
            elif input_type == 'Kilogram':
                Gram = float(input_val) * 1000
                Ton = float(input_val) / 1000
                Milligram = Gram * 1000
                Quintal = float(input_val) / 100
                weights = ['Ton', 'Quintal', 'Gram', 'Milligram']
                val = [Ton, Quintal, Gram, Milligram]
                results = {area: val for area, val in zip(weights, val)}
                print(results)
                self.ids.text_box_output.text = str(round(results[output_type], 5))
            elif input_type == 'Gram':
                Kilogram = float(input_val) / 1000
                Ton = Kilogram / 1000
                Milligram = float(input_val) * 1000
                Quintal = Kilogram * 100
                weights = ['Ton', 'Quintal', 'Kilogram', 'Milligram']
                val = [Ton, Quintal, Kilogram, Milligram]
                results = {area: val for area, val in zip(weights, val)}
                print(results)
                self.ids.text_box_output.text = str(round(results[output_type], 5))
            elif input_type == 'Milligram':
                Gram = float(input_val) / 1000
                Kilogram = Gram / 1000
                Ton = Kilogram / 1000
                Quintal = Kilogram * 100
                weights = ['Ton', 'Quintal', 'Kilogram', 'Gram']
                val = [Ton, Quintal, Kilogram, Gram]
                results = {area: val for area, val in zip(weights, val)}
                print(results)
                self.ids.text_box_output.text = str(round(results[output_type], 5))

    def get_gold_conversion_result(self):
        gold_values = ['Gram', 'Kilogram', 'Savaran', 'Tola']
        input_val = self.ids.text_box_input.text
        input_type = self.ids.spinner_conversion_input_type.text
        output_type = self.ids.spinner_conversion_output_type.text
        if input_val.replace('.', '').isdigit():
            if input_type == 'Gram':
                Savaran = float(input_val) / 8
                Kilogram = float(input_val) / 1000
                Tola = float(input_val) / 11.6638038
                gold_weights = ['Kilogram', 'Savaran', 'Tola']
                val = [Kilogram, Savaran, Tola]
                results = {area: val for area, val in zip(gold_weights, val)}
                print(results)
                self.ids.text_box_output.text = str(round(results[output_type], 5))
            elif input_type == 'Kilogram':
                Gram = float(input_val) * 1000
                Savaran = Gram / 8
                Tola = Gram / 11.6638038
                gold_weights = ['Gram', 'Savaran', 'Tola']
                val = [Gram, Savaran, Tola]
                results = {area: val for area, val in zip(gold_weights, val)}
                print(results)
                self.ids.text_box_output.text = str(round(results[output_type], 5))
            elif input_type == 'Savaran':
                Gram = float(input_val) * 8
                Kilogram = Gram / 1000
                Tola = Gram / 11.6638038
                gold_weights = ['Gram', 'Kilogram', 'Tola']
                val = [Gram, Kilogram, Tola]
                results = {area: val for area, val in zip(gold_weights, val)}
                print(results)
                self.ids.text_box_output.text = str(round(results[output_type], 5))
            elif input_type == 'Tola':
                Gram = float(input_val) * 11.6638038
                Kilogram = Gram / 1000
                Savaran = Gram * 8
                gold_weights = ['Gram', 'Kilogram', 'Savaran']
                val = [Gram, Kilogram, Savaran]
                results = {area: val for area, val in zip(gold_weights, val)}
                print(results)
                self.ids.text_box_output.text = str(round(results[output_type], 5))


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("calci.kv")


class CalculatorApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    CalculatorApp().run()
