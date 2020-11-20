
from Res.task7_func import change_words

words = ["się", "Się", "i", "I", "oraz", "Oraz", "nigdy", "Nigdy", "dlaczego", "Dlaczego"]
replacements = ["się", "Się", "oraz", "Oraz", "i", "I", "prawie nigdy", "Prawie nigdy", "czemu", "Czemu"]

path = r"D:\PycharmProjects\PWJSPiLB\Res\test.txt"

change_words(words, replacements, path)
