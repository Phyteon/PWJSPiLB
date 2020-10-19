# Script that asks user about their full name & year of birth


def inf_finder(idx, str):
    i = idx
    out = ''
    lim = len(str)

    while str[i].isalnum():
        out = out + str[i]
        i = i + 1
        if i == lim:
            break
    return out, i


def gibberish_ignore(idx, str):
    i = idx
    while not str[i].isalnum():
        i = i + 1
    return i


def spy():
    print('Please specify your full name and year of birth:\n')
    ans = input('Write your first name first, then last name and lastly year of birth\n')
    data = {'f_name': '', 'l_name': '', 'year': ''}
    index = 0
    for k, l in data.items():
        index = gibberish_ignore(index, ans)
        data[k], index = inf_finder(index, ans)
    print('Your first name is {0}, your last name is {1} and you were born in {2}'.format(data['f_name'],
                                                                                          data['l_name'], data['year']))
    return data


if __name__ == '__main__':
    spy()

