"""
Asymmetric RSA cryptosystem implementation using integer number theory.
Handles key generation, block-based message encryption, and decryption.
"""

from crypto_core.math_utils import gcd, mod_inverse, power_mod
from crypto_core.primes import is_prime

class RSASystem:
    """
    Encapsulates asymmetric RSA cryptographic operations.
    """
    def __init__(self, p: int, q: int):
        if not (is_prime(p) and is_prime(q)):
            raise ValueError("Parameters p and q must both be prime integers.")
        if p == q:
            raise ValueError("Primes p and q must be distinct.")
        
        self.p = p
        self.q = q
        self.n = p * q
        self.phi = (p - 1) * (q - 1)
        self.public_key, self.private_key = self._generate_keypair()

    def _generate_keypair(self) -> tuple[tuple[int, int], tuple[int, int]]:
        """
        Derives public (e, n) and private (d, n) key pairs.
        """
        # Standard candidate public exponents
        candidates = [65537, 17, 7, 5, 3]
        e = None
        for cand in candidates:
            if cand < self.phi and gcd(cand, self.phi) == 1:
                e = cand
                break
        
        if e is None:
            for cand in range(3, self.phi, 2):
                if gcd(cand, self.phi) == 1:
                    e = cand
                    break

        if e is None:
            raise RuntimeError("Failed to determine a valid coprime public exponent e.")

        d = mod_inverse(e, self.phi)
        if d is None:
            raise RuntimeError("Failed to compute modular inverse for private key d.")

        return (e, self.n), (d, self.n)

    def encrypt_block(self, message_int: int) -> int:
        """Encrypts an integer message block: c = (m^e) % n."""
        if message_int >= self.n:
            raise ValueError(f"Message integer ({message_int}) must be strictly less than modulus n ({self.n}).")
        e, n = self.public_key
        return power_mod(message_int, e, n)

    def decrypt_block(self, cipher_int: int) -> int:
        """Decrypts a ciphertext block: m = (c^d) % n."""
        d, n = self.private_key
        return power_mod(cipher_int, d, n)

    def encrypt_text(self, plaintext: str) -> list[int]:
        """Encrypts a string message into a sequence of RSA cipher integers."""
        encrypted_blocks = []
        for ch in plaintext:
            m = ord(ch)
            encrypted_blocks.append(self.encrypt_block(m))
        return encrypted_blocks

    def decrypt_text(self, cipher_blocks: list[int]) -> str:
        """Decrypts a sequence of RSA cipher integers back into plaintext."""
        decrypted_chars = []
        for block in cipher_blocks:
            m = self.decrypt_block(block)
            decrypted_chars.append(chr(m))
        return "".join(decrypted_chars)