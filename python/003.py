"""The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?"""


def solution(n):
    prime_factor = 1
    f = 3
    while n != 1:
        while not n % f: # factor the number with all odd integers increasing. if input were even, we'd have to do the same for evens
            prime_factor = f
            n = n / f 
        f = f + 2
    
    return prime_factor

if __name__ == '__main__':
    print(solution(600851475143))
