import generator
import time
FIXED_SYMBOL = '+'

# total of 5040 combinations (10P4) for each of the symbols

def special_cases(numbers):
    if ([1, 2, 3, 4] in numbers):
        return ''

def divide(numbers):
    return 'NAH'

def multiply(numbers):
    if (3 in numbers):
        if (8 in numbers):
            return 'OK 3 x 8'
    if (4 in numbers):
        if (6 in numbers):
            return 'OK 4 x 6'
    else: return 'NAH'

def minus(numbers):
    return 'NAH'

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
    if (2 in numbers):
        if ((0 in numbers) and (4 in numbers)):
            return 'OK 20 + 4'
        if ((1 in numbers) and (3 in numbers)):
            return 'OK 21 + 3'
    # 9 cases
    if (8 in numbers or 9 in numbers):
        if (sum(numbers) == 24):
            return 'OK add all'
    else: return 'NAH'

def main():
    symbol, numbers_raw = generator.generate(symbol = FIXED_SYMBOL)
    print(symbol, numbers_raw)
    start = time.process_time()
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
    elapsed = time.process_time() - start
    print(f'Time Elapsed: {elapsed}')
    print(ans)

main()