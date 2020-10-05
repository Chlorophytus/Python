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
from math import log10
from itertools import product
from typing import Tuple, Optional

MAX_BRUTE_FORCE_LOG: int = 6


def sieve_of_eratosthenes(maximum: int) -> [int]:
    """
    https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
    """
    sieve: [int] = [*range(2, maximum)]
    primes: [int] = []
    while len(sieve) > 0:
        primes.append(sieve[0])
        sieve = [s for s in sieve[1:] if s % sieve[0] != 0]
    return primes


def digit_combinations(logarithm: int) -> [Tuple[Optional[int]]]:
    """
    Return combinations of wildcard None and digits for parameter `logarithm`.

    :param logarithm The length of the tuples returned.
    """
    def splice(candidates: Tuple[Optional[int]]) -> Tuple[Optional[int]]:
        return tuple((10 ** (logarithm - n - 1) * d if d is not None else None for n, d in enumerate(candidates)))
    return (i for i in map(splice, product([None, *range(0, 10)], repeat=logarithm)) if i.count(None) > 1)


PRIMES_CACHE: [int] = sieve_of_eratosthenes(2 ** MAX_BRUTE_FORCE_LOG)
DIGITS_CACHE: [Tuple[Optional[int]]] = [*digit_combinations(MAX_BRUTE_FORCE_LOG)]


def solution():
    for digit_combination in DIGITS_CACHE:
        logarithm_candidates: [int] = [
            n for n, i in enumerate(digit_combination) if i is None]
        logarithm_fusion_bases: [int] = range(10)
        number_fusion: int = sum(
            [c for c in digit_combination if c is not None])
        for n, i in enumerate(logarithm_fusion_bases):
            i = sum([10 ** candidate * n for candidate in logarithm_candidates])
        accumulator: int = 0
        number: Optional[int] = None
        for i in logarithm_fusion_bases:
            if number_fusion + i in PRIMES_CACHE:
                accumulator += 1
                if number is None:
                    number = number_fusion + i
        if accumulator > 5:
            return number
    return None


if __name__ == "__main__":
    print(solution())
