"""
CryptoCore Package
A modular discrete mathematics and cryptographic computation toolkit.
"""

from crypto_core.math_utils import gcd, lcm, extended_gcd, mod_inverse, power_mod, int_sqrt, smallest_divisor
from crypto_core.primes import is_prime, generate_primes, prime_factors, euler_totient
from crypto_core.conversions import (
    char_to_ascii,
    ascii_to_char,
    decimal_to_base,
    base_to_decimal,
    reverse_array,
    partition_array,
    remove_duplicates,
    find_kth_smallest,
)
from crypto_core.ciphers import caesar_cipher, affine_encrypt, affine_decrypt, atbash_cipher
from crypto_core.rsa_engine import RSASystem

__all__ = [
    "gcd",
    "lcm",
    "extended_gcd",
    "mod_inverse",
    "power_mod",
    "int_sqrt",
    "smallest_divisor",
    "is_prime",
    "generate_primes",
    "prime_factors",
    "euler_totient",
    "char_to_ascii",
    "ascii_to_char",
    "decimal_to_base",
    "base_to_decimal",
    "reverse_array",
    "partition_array",
    "remove_duplicates",
    "find_kth_smallest",
    "caesar_cipher",
    "affine_encrypt",
    "affine_decrypt",
    "atbash_cipher",
    "RSASystem",
]