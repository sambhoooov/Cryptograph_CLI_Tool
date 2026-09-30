"""
Mathematical utilities implementing discrete mathematics algorithms from CSE1021 Unit 4:
Factoring methods, Euclidean GCD, Modular Inverses, and Modular Exponentiation.
"""

def gcd(a: int, b: int) -> int:
    """
    Euclidean Algorithm to find the Greatest Common Divisor of two integers.
    Time Complexity: O(log(min(a, b)))
    """
    a, b = abs(a), abs(b)
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a: int, b: int) -> int:
    """
    Computes the Least Common Multiple using integer division.
    lcm(a, b) = |a * b| // gcd(a, b)
    """
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)


def extended_gcd(a: int, b: int) -> tuple[int, int, int]:
    """
    Extended Euclidean Algorithm.
    Returns (g, x, y) such that a*x + b*y = g = gcd(a, b).
    """
    if b == 0:
        return abs(a), 1 if a >= 0 else -1, 0
    g, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return g, x, y


def mod_inverse(a: int, m: int) -> int | None:
    """
    Computes the modular multiplicative inverse of a modulo m using Extended GCD.
    Returns x such that (a * x) % m == 1.
    Returns None if gcd(a, m) != 1 or m <= 1.
    """
    if m <= 1:
        return None
    g, x, _ = extended_gcd(a, m)
    if g != 1:
        return None
    return (x % m + m) % m


def power_mod(base: int, exponent: int, modulus: int) -> int:
    """
    Computes (base^exponent) % modulus using fast repeated squaring.
    Time Complexity: O(log exponent)
    """
    if modulus == 1:
        return 0
    result = 1
    base = base % modulus
    exp = exponent

    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % modulus
        exp //= 2
        base = (base * base) % modulus

    return result


def int_sqrt(n: int) -> int:
    """
    Computes floor(sqrt(n)) using integer Newton-Raphson approximation.
    Does not require the external math library.
    """
    if n < 0:
        raise ValueError("Cannot compute real square root of a negative integer.")
    if n == 0:
        return 0
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x


def smallest_divisor(n: int) -> int:
    """
    Finds the smallest non-trivial divisor (> 1) of an integer n.
    """
    n = abs(n)
    if n < 2:
        return n
    if n % 2 == 0:
        return 2
    limit = int_sqrt(n)
    for d in range(3, limit + 1, 2):
        if n % d == 0:
            return d
    return n