"""
Comprehensive automated unit test suite.
Executes testing across all mathematical, conversion, cipher, and RSA modules.
Run using: python3 -m unittest tests/test_crypto.py
"""

import unittest
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


class TestCryptoCore(unittest.TestCase):
    # --- Math Utils ---
    def test_gcd_and_lcm(self):
        self.assertEqual(gcd(54, 24), 6)
        self.assertEqual(gcd(17, 31), 1)
        self.assertEqual(lcm(12, 18), 36)
        self.assertEqual(lcm(0, 5), 0)

    def test_extended_gcd_and_mod_inverse(self):
        g, x, y = extended_gcd(30, 20)
        self.assertEqual(g, 10)
        self.assertEqual(30 * x + 20 * y, 10)
        
        # Modular inverse of 3 mod 11 is 4 (3 * 4 = 12 = 1 mod 11)
        self.assertEqual(mod_inverse(3, 11), 4)
        # Not coprime: modular inverse must be None
        self.assertIsNone(mod_inverse(6, 9))

    def test_power_mod(self):
        self.assertEqual(power_mod(2, 10, 1000), 24)
        self.assertEqual(power_mod(7, 256, 13), 9)

    def test_int_sqrt_and_divisor(self):
        self.assertEqual(int_sqrt(144), 12)
        self.assertEqual(int_sqrt(150), 12)
        self.assertEqual(smallest_divisor(77), 7)
        self.assertEqual(smallest_divisor(13), 13)

    # --- Primes ---
    def test_primality_and_factors(self):
        self.assertFalse(is_prime(1))
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(97))
        self.assertFalse(is_prime(100))
        self.assertEqual(generate_primes(10, 30), [11, 13, 17, 19, 23, 29])
        self.assertEqual(prime_factors(84), [2, 2, 3, 7])

    def test_euler_totient(self):
        self.assertEqual(euler_totient(9), 6)
        self.assertEqual(euler_totient(13), 12)
        self.assertEqual(euler_totient(35), 24)

    # --- Conversions & Array Techniques ---
    def test_conversions(self):
        txt = "ABC"
        arr = char_to_ascii(txt)
        self.assertEqual(arr, [65, 66, 67])
        self.assertEqual(ascii_to_char(arr), txt)
        self.assertEqual(decimal_to_base(255, 16), "FF")
        self.assertEqual(decimal_to_base(10, 2), "1010")
        self.assertEqual(base_to_decimal("FF", 16), 255)

    def test_array_techniques(self):
        self.assertEqual(reverse_array([1, 2, 3, 4]), [4, 3, 2, 1])
        less, geq = partition_array([5, 1, 9, 3, 7], 5)
        self.assertEqual(less, [1, 3])
        self.assertEqual(geq, [5, 9, 7])
        self.assertEqual(remove_duplicates([1, 2, 2, 3, 1]), [1, 2, 3])
        self.assertEqual(find_kth_smallest([7, 10, 4, 3, 20, 15], 3), 7)

    # --- Ciphers ---
    def test_ciphers(self):
        raw = "Hello World!"
        c_enc = caesar_cipher(raw, shift=3)
        self.assertEqual(c_enc, "Khoor Zruog!")
        self.assertEqual(caesar_cipher(c_enc, shift=3, decrypt=True), raw)

        aff_enc = affine_encrypt("ATTACK AT DAWN", a=5, b=8)
        self.assertEqual(affine_decrypt(aff_enc, a=5, b=8), "ATTACK AT DAWN")

        self.assertEqual(atbash_cipher("Abc-123"), "Zyx-123")

    # --- Asymmetric RSA System ---
    def test_rsa_system(self):
        rsa = RSASystem(p=61, q=53)
        msg = "Hi"
        blocks = rsa.encrypt_text(msg)
        recovered = rsa.decrypt_text(blocks)
        self.assertEqual(recovered, msg)


if __name__ == "__main__":
    unittest.main()