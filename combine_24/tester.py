from ctypes import sizeof
import calculate
min, max = 0, 9
nums = []

def all_nums():
    i1 = min
    while i1 <= max:
        i2 = min + 1
        while i2 <= max:
            if (i2 > i1):
                i3 = min + 2
                while i3 <= max:
                    if (i3 > i2):
                        i4 = min + 3
                        while i4 <= max:
                            if (i4 > i3):
                                num = [i1, i2, i3, i4]
                                nums.append(num)
                            i4 += 1
                    i3 += 1
            i2 += 1
        i1 += 1
    return nums

def test_plus(nums):
    count_success = 0
    for num in nums:
        ans = calculate.plus(num)
        if ans != 'NAH': count_success += 1 
        print(f'{num}: {ans}')
    print(f'Success: {count_success}')

test_plus(all_nums())