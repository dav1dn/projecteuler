"""The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum."""

# There's probably a method to simplify the sum mathematically, but I'm feeling lazy, so..



def enumerated(n):
    """Returns the difference between sums of squares and square of sum."""
    return sum(range(1,n + 1)) ** 2 - sum(i * i for i in range(1,n + 1))

solution = enumerated

import time
if __name__ == '__main__':
    start = time.time()
    sol = solution(100)
    print("answer {0} found in {1} seconds".format(sol, time.time() - start))

