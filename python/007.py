"""By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?"""

# One method is counting up and factoring each number to see if it's a prime or not.

def is_prime(n):
    if not n % 2:
        return False # even numbers aren't primes yo
    else:
        i = 3
        while i < n ** 0.5 + 1:
            if not n % i:
                return False
            i += 2
        return True

def method_a(n):
    prime, test, count = 1, 3, 1
    while count < n:
        if is_prime(test):
            prime, count = test, count + 1
        test += 2
    return prime

# A second method would be to use a sieve method, like the sieve of Atkin... but I'm too lazy


solution = method_a
import time
if __name__ == '__main__':
    start = time.time()
    sol = solution(10001)
    print("answer {0} found in {1} seconds".format(sol, time.time() - start))


