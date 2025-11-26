class IntegerToRoman:
    def __init__(self, number):
        """Constructor: initializes the object with an integer value."""
        self.number = number

    def convert(self):
        """Converts the stored integer to a Roman numeral."""
        value_map = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]

        num = self.number
        roman = ""

        for value, symbol in value_map:
            while num >= value:
                roman += symbol
                num -= value

        return roman


# --- Example Usage ---
if __name__ == "__main__":
    number = int(input("Enter an integer: "))
    converter = IntegerToRoman(number)  # Creating an object
    print("Roman numeral:", converter.convert())
