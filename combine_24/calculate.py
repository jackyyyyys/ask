import generator
import time
FIXED_SYMBOL = '+'

# total of 5040 combinations (10P4) for each of the symbols

def special_cases(numbers):
    if ([1, 2, 3, 4] in numbers):
        # + * / OK
        return 'OK just 1234 = ='

# 24 x2{X} = 4{X}8
# 24 x3 = 72{X}
# 24 x4{X} = 96
# only /3 possible
# DONE =_=
def divide(numbers):
    if (3 in numbers and 6 in numbers and 9 in numbers):
        return 'OK 96 / 3'
    else: return 'NAH'

# DONE actually so little
def multiply(numbers):
    # _x_x_ -> 2x3x4 -> 1 case
    if (2 in numbers and 3 in numbers and 4 in numbers):
        return 'OK 2 x 3 x 4'

    # _x_ -> 3x8 or 4x6 -> 2 case
    if (3 in numbers and 8 in numbers):
        return 'OK 3 x 8'
        
    if (4 in numbers and 6 in numbers):
        return 'OK 4 x 6'

    else: return 'NAH'

# a bit more complicated, but later will find out no
def minus(numbers):
    # 2-digit - 1-digit - 1-digit

    # 2-digit - 1-digit
    # 24 + (anything > 6) = >30
    # --> 6 3 0, 7 3 1, 8 3 2, 9 3 3(X)                 => 0 3 6, 1 3 7, 2 3 8 
    # --> 0 2 4, 1 2 5, 2 2 6(X), 3 2 7, 4 2 8, 5 2 9   => 0 2 4, 1 2 5, 2 3 7, 2 4 8, 2 5 9
    if(2 in numbers or 3 in numbers):
        print('next')

    # 2-digit - 2-digit
    # cannot +10 -> from +11

    return 'NAH'

# DONE
def plus(numbers):
    # 3 1-digit add up -> 1 case
    if (7 in numbers and 8 in numbers and 9 in numbers):
        return 'OK 7 + 8 + 9'
    # 2-digit + 1 digit -> 2x2x2 = 8 cases
    if (1 in numbers):
        if ((5 in numbers) and (9 in numbers)):
            return 'OK 15 + 9'
        if ((6 in numbers) and (8 in numbers)):
            return 'OK 16 + 8'
        else: return 'NAH'
    if (2 in numbers):
        if ((0 in numbers) and (4 in numbers)):
            return 'OK 20 + 4'
        if ((1 in numbers) and (3 in numbers)):
            return 'OK 21 + 3'
        else: return 'NAH'
    # 4 1-digit add up -> 9 cases
    if (8 in numbers or 9 in numbers):
        if (sum(numbers) == 24):
            return 'OK add all'
        else: return 'NAH'
    else: return 'NAH'

def calculate_unsorted(numbers):
    return 0

def calculate_sorted(numbers):
    return 0

def main():
    symbol, numbers_raw = generator.generate(symbol = FIXED_SYMBOL)
    print(symbol, numbers_raw)
    numbers_sorted = sorted(numbers_raw)
    special_cases(numbers_sorted)
    if (symbol == "+"):
        ans = plus(numbers_sorted)
    elif (symbol == "-"):
        ans = minus(numbers_sorted)
    elif (symbol == "*"):
        ans = multiply(numbers_sorted)
    elif (symbol == "/"):
        ans = divide(numbers_sorted)
    print(f'Answer: {ans}')

# main()