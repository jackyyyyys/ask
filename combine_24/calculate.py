import generator
import time
FIXED_SYMBOL = '+'

# total of 5040 combinations (10P4) for each of the symbols

def special_cases(numbers):
    if ([1, 2, 3, 4] in numbers):
        # + * / OK
        return 'OK just 1234 = ='

# DONE
def divide(numbers):
    # 24 x2 = 48 -> 2 4 8
    # 24 x3 = 72 -> 2 3 7
    # 24 x4 = 96 -> 4 6 9
    if (2 in numbers and 3 in numbers and 7 in numbers):
        return 'OK 72 / 3'
    if (2 in numbers and 4 in numbers and 8 in numbers):
        return 'OK 48 / 2'
    if (4 in numbers and 6 in numbers and 9 in numbers):
        return 'OK 96 / 4'
    else: return 'NAH'

# DONE
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
    # 29 - 1 - 4                                                            1249        2 914
    # 30 - 1 - 5, 30 - 2 - 4, 30 - 3 - 3{X}                                 0135 0234   3 015 3 024
    # 31 - 1 - 6{X}, 31 - 2 - 5, 33 - 3 - 4{X}                              1235        3 125
    # 32 - 1 - 7, 32 - 2 - 6{X}, 32 - 3 - 5{X}, 32 - 4 - 4{X}               1237        3 217
    # 33{X}
    # 34 - 1 - 9, 34 - 2 - 8, 34 - 3 - 7{X}, 34 - 4 - 6{X}, 34 - 5 - 5{X}   1349 2348   3 419 3 428
    # 35 - 2 - 9, 35 - 3 - 8{X}, 35 - 4 - 7, 35 - 5 - 6{X}                  2359 3457   3 529 3 547
    # 36 - 3 - 9{X}, 36 - 4 - 8, 36 - 5 - 7, 36 - 6 - 6{X}                  3469 3567   3 648 3 657
    # 37 - 4 - 9, 37 - 5 - 8, 37 - 6 - 7{X}                                 3479 3578   3 749 3 758
    # 38 - 5 - 9, 38 - 6 - 8{X}, 38 - 7 - 7{X}                              3589        3 859
    # 39 - 6 - 9{X}, 39 - 7 - 8                                             3789        3 978


    # 2-digit - 1-digit
    # 24 + (anything > 6) = >30
    # --> 6 3 0, 7 3 1, 8 3 2, 9 3 3(X)                 => 0 3 6, 1 3 7, 2 3 8 
    # --> 0 2 4, 1 2 5, 2 2 6(X), 3 2 7, 4 2 8, 5 2 9   => 0 2 4, 1 2 5, 2 3 7, 2 4 8, 2 5 9
    if(2 in numbers or 3 in numbers):
        print('next')

    # 2-digit - 2-digit
    # cannot +10 +11 -> from +12
    # 11 35(X), 12 36, 13 37(X), 14 38, 15 39, 16 40, 17 41(X), 18 42, 19 43
    # 21 45, 22 46(X), 23 47, 24 48(X), 25 49, 26 50, 27 51, 28 52, 29 53
    # 31 55(X), 32 56, 33 57(X), 34 58, 35 59(X), 36 60(X), 37 61, 38 62, 39 63(X)
    # 41 65, 42 66(X), 43 67, 44 68(X), 45 69, 46 70, 47 71(X), 48 72, 49 73
    # 51 75(X), 52 76, 53 77(X), 54 78, 55 79(X), 56 80, 57 81, 58 82(X), 59 83
    # 61 85, 62 86(X), 63 87, 64 88(X), 65 89, 66 90(X), 67 91, 68 92, 69 93(X)
    # 71 95, 72 96, 73 97(X), 74 98, 75 99(X)

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
    symbol, numbers_raw = generator.generate(symbol = FIXED_SYMBOL)

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

main()