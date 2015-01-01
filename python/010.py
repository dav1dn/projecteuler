"""The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million."""
import itertools
import time

# sieve of eratosthenes method

numbers = [True] * 2000000

def sieve(numbers, x):
    # mark all multiples of x as not prime
    for i in range(2 * x, len(numbers), x):
        numbers[i] = False

def solution():
    for n in range(2, int(len(numbers) ** 0.5) + 1):
        if numbers[n]:
            sieve(numbers, n)
    return sum(i for i in range(2, len(numbers)) if numbers[i])


if __name__ == '__main__':
    now = time.time()
    sol = solution()
    print("answer {0} found in {1} seconds".format(sol,  time.time() - now))
