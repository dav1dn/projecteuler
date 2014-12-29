"""A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers."""

import time

def is_palindrome(n):
    # Sorta hacky way to determine if a number is a palindrome.
    return str(n) == str(n)[::-1]

def three_digit_multiples_of_11():
    lst = [11*n for n in range(10,100)]
    return [n for n in lst if len(str(n)) == 3]

def solution():
    # Each even-digited palindrome is divisible by 11, so we'll use multiples of 11.
    # Proof: http://jwilson.coe.uga.edu/emt669/Student.Folders/Bacchus.Mohamed/pal/pal.html
    # We'll bruteforce each 3 digit multiple of 11 with each 3 digit number. 
    # This is pretty inefficient...
    largest_palindrome = 1

    for x in three_digit_multiples_of_11()[::-1]:
        for y in list(range(100,999))[::-1]:
            product = x * y
            if product < largest_palindrome: # because we count down, break out of y loop if no more valid sol
                break
            elif is_palindrome(product) and product > largest_palindrome:
                largest_palindrome = product
    return largest_palindrome
    

    
if __name__ == '__main__':
    start = time.time()
    answer = solution()
    print("answer {0} found in {1} seconds".format(answer, time.time() - start))
