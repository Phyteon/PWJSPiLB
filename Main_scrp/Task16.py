from Res.task16_func import parse_calc_input

print("Please write your equation here: \n")
equation = input()
out = parse_calc_input(equation)
if out == False:
    print("You have made a mistake in syntax")
else:
    print(out)