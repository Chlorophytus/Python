"""
Problem Statement:

By replacing the 1st digit of the 2-digit number *3, it turns out that six of
the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit
number is the first example having seven primes among the ten generated
numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and
56993. Consequently 56003, being the first member of this family, is the
smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily
adjacent digits) with the same digit, is part of an eight prime value family.
"""
import math


"""
https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
"""
def sieve_of_eratosthenes(maximum: int) -> [int]:
    sieve: [int] = [*range(2, maximum)]
    primes: [int] = []
    while len(sieve) > 0:
        primes.append(sieve[0])
        sieve = [s for s in sieve[1:] if not s % sieve[0] == 0]
    return primes
        
    # composites: [[int]] = []
    # for n in range(2, math.isqrt(maximum)):
    #     composites.append([m for m in range(n, maximum) if m % n == 0])
    # sieve: [int] = [c for deep in composites for c in deep]
    # return sorted([prime for prime in sieve if sieve.count(prime) == 1])

def get_digit_combinations(comb: int) -> [[int]]:
    log10: int = round(math.log10(comb) - 0.5) + 1
    combinations: [[int]] = []
    for digit in range(0, log10):
        this_digit: int = 10 ** digit
        combinations.append([d for d in range(
            this_digit, this_digit * 10, this_digit)])
    return combinations


def solution():
    pass
    # sieve: [int] = sieve_of_eratosthenes(10000)
    # for i in range(10, 56003):
    #     primes = sieve_of_eratosthenes(i)


if __name__ == "__main__":
    print(solution())
