from converter import PhraseConverter
from codes import CODE
from ui import ConverterInterface

# Initialize converter
converter = PhraseConverter(code=CODE)
# Initialize UI
useri = ConverterInterface(converter=converter)


