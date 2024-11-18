from tkinter import *
from converter import PhraseConverter


class ConverterInterface:

    def __init__(self, converter: PhraseConverter):
        # Initialize converter
        self.converter = converter

        # Create UI window
        self.window = Tk()
        self.window.title("Converter")
        self.window.config(padx=20, pady=20)
        self.window.minsize(width=500, height=300)

        # Create heading
        self.heading = Label(text="Welcome to the Morse Code Converter!",
                             font=("Courier", 20, "bold"))
        self.heading.grid(column=0, row=0, columnspan=3, padx=20, pady=20)

        # Create subheading
        self.directions = Label(text="Excepts any alphabet numbers, and 0-9 in numbers. No special characters please!",
                                font=("Courier", 12))
        self.directions.grid(column=0, row=1, columnspan=3, padx=20, pady=20)

        # Create first text-box label
        self.entry_label = Label(text="Type word to be converted: ",
                                 font=("Courier", 12))
        self.entry_label.grid(column=0, row=2, columnspan=1, padx=5, pady=5)

        # Create text-box for user to enter their word or phrase to be converted
        self.user_input = Entry(width=100)
        self.user_input.grid(column=1, row=2, columnspan=2)

        # Create second text-box label
        self.convert_label = Label(text="Your converted word: ",
                                   font=("Courier", 12))
        self.convert_label.grid(column=0, row=3, columnspan=1, padx=5, pady=5)

        # Create text-box for converted morse code to be displayed
        self.translated = Entry(width=100)
        self.translated.grid(column=1, row=3, columnspan=2)

        # Create button to call functionality that converts the user's word or phrase into morse code
        self.convert_button = Button(
            text="Convert",
            font="Courier",
            bg="light gray",
            command=lambda: self.display_conversion(user_entry=self.user_input))
        self.convert_button.grid(column=1, row=4, ipadx=10, pady=10)

        # Establish loop that keeps UI open until the user closes it
        self.window.mainloop()

    def display_conversion(self, user_entry):
        '''Displays the morse code that corresponds to the given word or phrase'''
        phrase = user_entry.get()
        converted_word = self.converter.convert_phrase(phrase=phrase)
        self.translated.delete(0, END)
        self.translated.insert(0, converted_word)


