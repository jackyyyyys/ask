import random
symbols = ['+', '-', '*', '/']

def generate(**kwargs):
    numbers = random.sample(range(10), 4)
    if 'symbol' in kwargs:
        symbol = kwargs['symbol']
    else:
        symbol = symbols[random.randint(0, 3)]
    return (symbol, numbers)