import enchant
import difflib
from enchant.checker import SpellChecker
from enchant import Dict
checker = SpellChecker("ru_RU")
dictionary = Dict("ru_RU")

checker.set_text("провиряю ошибки в тиксте")

for err in checker:
    print("ERROR:", err.word)
