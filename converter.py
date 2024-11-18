
class PhraseConverter:
    def __init__(self, code):
        self.code = code
        self.converted_phrase = ""

    def insert_space(self, current_letnum, phrase):
        '''Inserts a dash to represent a difference in characters'''
        if phrase.index(current_letnum) < (len(phrase) - 1) \
                and phrase[phrase.index(current_letnum) + 1] != " ":
            return " / "
        else:
            return ""

    def convert_phrase(self, phrase):
        '''Converts english word or phrase into morse code using a dictionary of alphabetic letters to codes'''

        # Checks that the converted_phrase variable is empty
        if self.converted_phrase != "":
            self.converted_phrase = ""

        # Iterates through each character and retrieves the associated code
        for letnum in phrase:
            if letnum in self.code.keys():
                converted_letter = self.code[letnum]
                # Concatenate each code with an inserted dash for easier viewing
                self.converted_phrase += (converted_letter + self.insert_space(
                    current_letnum=letnum,
                    phrase=phrase)
                                          )
            # Insert a double dash to represent a space between words
            elif letnum == " ":
                self.converted_phrase += " // "
            else:
                return "Word or phrase not translatable"
        return self.converted_phrase
