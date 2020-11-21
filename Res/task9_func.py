

def str_to_complex(string):
    split_in = []
    for symbol in string:
        if symbol == " ":
            pass
        else:
            split_in.append(symbol)
    itr = 0
    real_str = []
    imag_str = []
    while (split_in[itr] != "+" and split_in[itr] != "-") or itr == 0:
        real_str.append(split_in[itr])
        itr += 1
    while itr != len(split_in) - 1:
        imag_str.append(split_in[itr])
        itr += 1
    real_str = "".join(real_str)
    imag_str = "".join(imag_str)
    real = float(real_str)
    imag = float(imag_str)
    z = complex(real, imag)
    return z