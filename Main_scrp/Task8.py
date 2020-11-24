
from Res.task7_func import change_words

change = {
        'i': 'oraz', 'I': 'Oraz', 'i,': 'oraz,', 'oraz': 'i', 'oraz,': 'i,',
        'nigdy': 'prawie nigdy', 'Nigdy': 'Prawie nigdy', 'Nigdy.': 'Prawie nigdy.', 'Nigdy,': '',
        'nigdy.': 'prawie nigdy.', 'nigdy,': 'prawie nigdy,', 'dlaczego': 'czemu', 'Dlaczego': '',
        'Dlaczego?': 'Czemu?', 'dlaczego.': 'czemu.', 'Dlaczego,': 'Czemu,', 'dlaczego,': 'czemu,',
        }

path = r"D:\PycharmProjects\PWJSPiLB\Res\test.txt"

change_words(change, path)
