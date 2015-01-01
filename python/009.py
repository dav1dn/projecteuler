"""A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc."""
import time

def solution(n):
    for i in range(1, n):
        for j in range(1, n):
            k = n - i - j
            if k < 0:
                break
            if i ** 2 + j ** 2 == k ** 2:
                return i * j * k

if __name__ == '__main__':
    now = time.time()
    sol = solution(1000)
    print("answer {0} found in {1} seconds".format(sol,  time.time() - now))

