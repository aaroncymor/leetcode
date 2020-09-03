def isPalindromeA(x):
    num = x
    while True:
        last = num % 10
        first = 0
        divide_by = 10        
        
        while True:
            res = num / divide_by
            #print("CURR RES", res)
            if res < 10:
                # if res is not less than 10, then result is
                # not one digit. we need to increase 10 to 100
                # to check if number is in the hundreds, and increase
                # 100 to 1000 if it is in the thousands. That is the pattern.
                first = res
                print(first, last)
                if first != last:
                    return False
                elif first == last:
                    middle = num - ((first * divide_by) + last)
                    middle /= 10
                    if middle < 10 and middle >= 0:
                        # case 1001, we get middle '00'
                        # or case 1 digit left for middle then we
                        # assume integer is palindrome.
                        return True

                    num = middle
                    break
            else:
                divide_by *= 10
                #print("DIVIDE BY", divide_by)


def isPalindromeB(x):
    # if x is less than zero,
    # and last digit of x is zero (you cant have a number that)
    # starts with zero
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    
    revertedNumber = 0
    while x > revertedNumber:
        # we basically try to get the half of the digit and
        # revert it, and compare with the other half 

        # current revertedNum value * 10 + (x % 10) or last digit
        revertedNumber = revertedNumber * 10 + (x % 10)
        x /= 10

    return (x == revertedNumber) or (x == revertedNumber / 10)


if __name__ == '__main__':
    #print(isPalindromeB(121))
    print(isPalindromeB(112211))