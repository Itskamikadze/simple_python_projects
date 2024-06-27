# Unit converter

# First, you need to ask person about type of unit

class UnitConverter():

    def __init__(self, unit) -> None:
        self.unit = unit

    def choose_temp(self):
        # choose two units
        temp_1 = input("""Please choose the type of temp units you need to convert: 
                     [C] - Celsius
                     [K] - Kelvin
                     [F] - Fahrenheit
                     """).capitalize()
        value = int(input("Please provide value: "))
        temp_2 = input("Please choose the second type of temp unit: ").capitalize()

        if temp_1 == "C" and temp_2 == "K":
            value += 275.15
        elif temp_1 == "C" and temp_2 == "F":
            value = (value * 1.8) + 32
        elif temp_1 == "K" and temp_2 == "C":
            value -= 275.15
        elif temp_1 == "F" and temp_2 == "C":
            value = (value - 32) / 1.8
        elif temp_1 == "F" and temp_2 == "K":
            value = (value + 459.67) * 0.555
        elif temp_1 == "K" and temp_2 == "F":
            value = (value * 1.80) - 459.67
        return f"Converted value is: {value}" 
    
    def choose_mass(self):
        # choose two mass units
        mass_1 = input("""Please choose the type of mass units you need to convert: 
                     [G] - gram
                     [D] - dag
                     [K] - kilogram
                     [T] - Tone
                     """).capitalize()
        value = int(input("Please provide value: "))
        mass_2 = input("Please choose the second type of mass unit: ").capitalize()

        if mass_1 == "G" and mass_2 == "D":
            value /= 10
        elif mass_1 == "D" and mass_2 == "G":
            value *= 10
        elif mass_1 == "G" and mass_2 == "K":
            value /= 1000
        elif mass_1 == "K" and mass_2 == "G":
            value *= 1000
        elif mass_1 == "G" and mass_2 == "T":
            value /= 1000000
        elif mass_1 == "T" and mass_2 == "G":
            value *= 1000000
        elif mass_1 == "D" and mass_2 == "K":
            value /= 100
        elif mass_1 == "K" and mass_2 == "D":
            value *= 100
        elif mass_1 == "D" and mass_2 == "T":
            value /= 100000
        elif mass_1 == "T" and mass_2 == "D":
            value *= 100000
        elif mass_1 == "K" and mass_2 == "T":
            value /= 1000
        elif mass_1 == "T" and mass_2 == "K":
            value *= 1000
        return f"Converted value is: {value}" 





if __name__ == "__main__":
    game_on = True
    while game_on:
        # when the game is still on

        unit = input("Put a unit that you need convert [T or M] or exit [E]: ").capitalize()
        conv_unit = UnitConverter(unit)
        #temperature
        if unit =="T":
            print(conv_unit.choose_temp())
        #mass
        elif unit =="M":
            print(conv_unit.choose_mass())
        elif unit =="E":
            print('Bye! Bye!')
            game_on = False
            break