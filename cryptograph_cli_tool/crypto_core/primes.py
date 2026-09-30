"""
Prime number algorithms covering CSE1021 Unit 4:
Primality verification, prime generation, prime factorization, and Euler's Totient.
"""

from crypto_core.math_utils import int_sqrt, smallest_divisor

def is_prime(n: int) -> bool:
    """
    Determines if n is prime in O(sqrt(n)) time complexity.
    Optimized by checking 2, 3, and 6k +/- 1 step boundaries.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    limit = int_sqrt(n)
    for i in range(5, limit + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


def generate_primes(start: int, end: int) -> list[int]:
    """
    Generates all prime numbers within the closed interval [start, end].
    """
    lower = max(2, start)
    return [num for num in range(lower, end + 1) if is_prime(num)]


def prime_factors(n: int) -> list[int]:
    """
    Computes the canonical prime factorization of integer n.
    Returns factors in non-decreasing order.
    """
    factors = []
    curr = abs(n)
    while curr > 1:
        d = smallest_divisor(curr)
        factors.append(d)
        curr //= d
    return factors


def euler_totient(n: int) -> int:
    """
    Computes Euler's Totient phi(n) using Euler's product formula:
    phi(n) = n * Product_{p|n} (1 - 1/p)
    """
    if n <= 0:
        return 0
    result = n
    temp = n
    p = 2
    while p * p <= temp:
        if temp % p == 0:
            while temp % p == 0:
                temp //= p
            result -= result // p
        p += 1
    if temp > 1:
        result -= result // temp
    return result