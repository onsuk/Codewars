'''
Define a function that takes in two numbers a and b and returns the last decimal digit of a^b. 
Note that a and b may be very large!

For example, the last decimal digit of 9^7 is 9, since 9^7 = 4782969. 
The last decimal digit of (2^200)^(2^300), which has over 10^92 decimal digits, is 6.

The inputs to your function will always be non-negative integers.

Examples
last_digit(4, 1)                # returns 4
last_digit(4, 2)                # returns 6
last_digit(9, 7)                # returns 9
last_digit(10, 10 ** 10)        # returns 0
last_digit(2 ** 200, 2 ** 300)  # returns 6
Remarks
JavaScript, C++, R
Since these languages don't have native arbitrarily large integers, your arguments are going to be strings representing non-negative integers.

'''


def last_digit(n1, n2):
    cycle = {
        0: [0,0,0,0],
        1: [1,1,1,1],
        2: [6,2,4,8],
        3: [1,3,9,7],
        4: [6,4,6,4],
        5: [5,5,5,5],
        6: [6,6,6,6],
        7: [1,7,9,3],
        8: [6,8,4,2],
        9: [1,9,1,9]
    }
    if n2==0:
        return 1

    return cycle[n1%10][n2%4]