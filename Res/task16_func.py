from Main_scrp.Task15 import Complex


def parse_calc_input(string):
    special = ["*", "/", "+", "-"]
    special_groups = [["*", "/"], ["+", "-"]]
    modified = []
    idx = 0
    while idx < len(string):
        if string[idx].isdigit():
            temp = []
            while string[idx].isdigit():
                temp.append(string[idx])
                idx += 1
                if idx == len(string):
                    break
            if idx == len(string):
                break
            str_num = ''.join(temp)
            num = float(str_num)
            if string[idx] == "i":
                z = Complex(0, num)
                modified.append(z)
            else:
                z = Complex(num, 0)
                modified.append(z)
        elif string[idx] in special:
            modified.append(string[idx])
        elif string[idx] == "(":
            nested = ""
            idx += 1
            while string[idx] != ")":
                nested += string[idx]
                idx += 1
                if idx == len(string):
                    print("Invalid syntax")
                    return False
            z = parse_calc_input(nested)
            modified.append(z)
            if idx == len(string):
                break
        elif string[idx] == " ":
            pass
        else:
            print("Invalid syntax")
            return False
        idx += 1
