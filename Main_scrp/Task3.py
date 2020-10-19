# This script checks if two strings match each other
code = 'literkaAliterkaGliterkaH'


def code_chck(pin):
    ans = input('Please give entry code:\n')
    while ans != pin:
        ans = input('Wrong code! Please try again:\n')
    print('Entry successful')


if __name__ == '__main__':
    code_chck(code)
