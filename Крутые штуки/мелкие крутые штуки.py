
# ---------------------------------------------------------------------
# время выполнения программы
import time

start_time = time.perf_counter()
"""тут какой-то код"""
end_time= time.perf_counter()
print(f'{end_time - start_time:.8f}')
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
from enchant.checker import SpellChecker
from enchant import Dict
checker = SpellChecker("ru_RU")
dictionary = Dict("ru_RU")

checker.set_text("провиряю ошибки в тиксте")

for err in checker:
    print("ERROR:", err.word)
# ---------------------------------------------------------------------