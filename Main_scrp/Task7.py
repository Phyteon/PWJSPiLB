
from Res.task7_func import change_words


path = r"D:\PycharmProjects\PWJSPiLB\Res\test.txt"

delete_instr = {'się': '', 'Się': '', 'się.': '', 'się,': '',
                '\nsię': '', '\nSię': '', '\nsię.': '', '\nsię,': '',
                'i': '', 'I': '', 'i,': '', 'oraz': '', 'oraz,': '',
                '\ni': '', '\nI': '', '\ni,': '', '\noraz': '', '\noraz,': '',
                'nigdy': '', 'Nigdy': '', 'Nigdy.': '', 'Nigdy,': '',
                '\nnigdy': '', '\nNigdy': '', '\nNigdy.': '', '\nNigdy,': '',
                'nigdy.': '', 'nigdy,': '', 'dlaczego': '', 'Dlaczego': '',
                '\nnigdy.': '', '\nnigdy,': '', '\ndlaczego': '', '\nDlaczego': '',
                'Dlaczego?': '', 'dlaczego.': '', 'Dlaczego,': '', 'dlaczego,': '',
                '\nDlaczego?': '', '\ndlaczego.': '', '\nDlaczego,': '', '\ndlaczego,': ''}

change_words(delete_instr, path)
