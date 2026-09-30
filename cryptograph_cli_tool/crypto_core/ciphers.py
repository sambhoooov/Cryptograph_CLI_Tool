"""
Classical symmetric ciphers implementing character math, modular arithmetic,
and substitution algorithms from CSE1021 Unit 3.
"""

from crypto_core.math_utils import gcd, mod_inverse

def caesar_cipher(text: str, shift: int, decrypt: bool = False) -> str:
    """
    Encrypts or decrypts text using Caesar shift substitution.
    Preserves letter casing and leaves non-alphabetical characters intact.
    """
    s = (-shift) % 26 if decrypt else shift % 26
    output = []
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            transformed = chr((ord(ch) - base + s) % 26 + base)
            output.append(transformed)
        else:
            output.append(ch)
    return "".join(output)


def affine_encrypt(text: str, a: int, b: int) -> str:
    """
    Encrypts plaintext via the Affine transformation: E(x) = (a*x + b) mod 26.
    Key 'a' must be coprime with 26.
    """
    if gcd(a, 26) != 1:
        raise ValueError(f"Key a ({a}) must be coprime with 26.")
    
    result = []
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            x = ord(ch) - base
            enc = (a * x + b) % 26
            result.append(chr(enc + base))
        else:
            result.append(ch)
    return "".join(result)


def affine_decrypt(text: str, a: int, b: int) -> str:
    """
    Decrypts ciphertext via inverse Affine transformation: D(y) = a^-1 * (y - b) mod 26.
    """
    if gcd(a, 26) != 1:
        raise ValueError(f"Key a ({a}) must be coprime with 26.")
    
    a_inv = mod_inverse(a, 26)
    if a_inv is None:
        raise ValueError(f"Modular inverse for a={a} mod 26 does not exist.")
    
    result = []
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            y = ord(ch) - base
            dec = (a_inv * (y - b)) % 26
            result.append(chr(dec + base))
        else:
            result.append(ch)
    return "".join(result)


def atbash_cipher(text: str) -> str:
    """
    Applies the classical Atbash symmetric substitution (A<->Z, B<->Y, etc.).
    """
    result = []
    for ch in text:
        if 'A' <= ch <= 'Z':
            result.append(chr(ord('Z') - (ord(ch) - ord('A'))))
        elif 'a' <= ch <= 'z':
            result.append(chr(ord('z') - (ord(ch) - ord('a'))))
        else:
            result.append(ch)
    return "".join(result)