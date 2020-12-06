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
            str_num = ''.join(temp)
            num = float(str_num)
            if idx != len(string):
                if string[idx] == "i":
                    z = Complex(0, num)
                    modified.append(z)
                else:
                    idx -= 1
                    z = Complex(num, 0)
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
                if string[idx] == "(":
                    while string[idx] != ")":
                        nested += string[idx]
                        idx += 1
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
    for priority_group in special_groups:
        for sym in priority_group:
            if sym in modified:
                while sym in modified:
                    sym_idx = modified.index(sym)
                    if priority_group == special_groups[0]:
                        if sym_idx == 0 or sym_idx == len(modified)-1:
                            print("Invalid syntax")
                            return False
                        if sym == "*":
                            zx = modified[sym_idx-1] * modified[sym_idx+1]
                            modified.pop(sym_idx)
                            modified.pop(sym_idx)
                            modified.pop(sym_idx-1)
                            modified.insert(sym_idx-1, zx)
                        else:
                            zx = modified[sym_idx - 1] / modified[sym_idx + 1]
                            modified.pop(sym_idx)
                            modified.pop(sym_idx)
                            modified.pop(sym_idx - 1)
                            modified.insert(sym_idx-1, zx)
                    else:
                        if sym_idx == len(modified)-1:
                            print("Invalid syntax")
                            return False
                        if sym == "+":
                            if sym_idx == 0:
                                print("Invalid syntax")
                                return False
                            zx = modified[sym_idx - 1] + modified[sym_idx + 1]
                            modified.pop(sym_idx)
                            modified.pop(sym_idx)
                            modified.pop(sym_idx - 1)
                            modified.insert(sym_idx - 1, zx)
                        else:
                            if sym_idx == 0:
                                zx = Complex(0, 0) - modified[1]
                                modified.pop(sym_idx)
                                modified.pop(sym_idx)
                                modified.insert(sym_idx, zx)
                            else:
                                zx = modified[sym_idx - 1] - modified[sym_idx + 1]
                                modified.pop(sym_idx)
                                modified.pop(sym_idx)
                                modified.pop(sym_idx - 1)
                                modified.insert(sym_idx - 1, zx)
    if len(modified) > 1:
        print("Error occured")
    return modified[0]
