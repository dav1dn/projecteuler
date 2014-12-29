"""2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"""

# Because 20 is divisible by 1, 2, 4, 5, 10, 20, remove all of these. Follow this logic for the rest of the factors.
factors = [11, 13, 14, 16, 17, 18, 19, 20]

# Multiple of all of the numbers from 1-20 also includes being a multiple of the LCM of #1-10, or 2520, so we'll only check
# each multiple of 2520.

import itertools
import time

def solution():
    for n in itertools.count(2520,2520):
        if all(not n % f for f in factors):
            return n
    return None


if __name__ == '__main__':
    start = time.time()
    sol = solution()
    print("answer {0} found in {1} seconds".format(sol, time.time() - start))

