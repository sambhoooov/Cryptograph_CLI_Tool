"""
Main Interactive CLI Application Driver
Entry point for the Cryptography & Number Theory Computational Suite.
"""

from crypto_core.math_utils import gcd, lcm, mod_inverse, power_mod, int_sqrt, smallest_divisor
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
from crypto_core.validator import get_int, get_string, get_choice


def run_math_menu():
    """Sub-menu handler for Number Theory and Factoring Tools."""
    while True:
        print("\n" + "-" * 40)
        print("  MODULE 1: NUMBER THEORY & FACTORING")
        print("-" * 40)
        print("1. Greatest Common Divisor (GCD) & LCM")
        print("2. Primality Verification")
        print("3. Prime Generator in Range")
        print("4. Canonical Prime Factorization")
        print("5. Modular Multiplicative Inverse")
        print("6. Fast Modular Exponentiation (a^b mod m)")
        print("7. Euler's Totient phi(n)")
        print("8. Integer Square Root & Smallest Divisor")
        print("0. Back to Main Menu")

        choice = get_choice("\nSelect an operation (0-8): ", {str(i) for i in range(9)})

        if choice == "1":
            a = get_int("Enter integer a: ")
            b = get_int("Enter integer b: ")
            print(f"[+] GCD({a}, {b}) = {gcd(a, b)}")
            print(f"[+] LCM({a}, {b}) = {lcm(a, b)}")
        elif choice == "2":
            n = get_int("Enter integer n: ")
            status = "PRIME" if is_prime(n) else "COMPOSITE / NON-PRIME"
            print(f"[+] {n} is {status}.")
        elif choice == "3":
            start = get_int("Enter start bound: ", min_val=2)
            end = get_int("Enter end bound: ", min_val=start)
            primes = generate_primes(start, end)
            print(f"[+] Primes in [{start}, {end}] (Count: {len(primes)}): {primes}")
        elif choice == "4":
            n = get_int("Enter integer (> 1): ", min_val=2)
            print(f"[+] Prime factorization of {n}: {prime_factors(n)}")
        elif choice == "5":
            a = get_int("Enter base a: ")
            m = get_int("Enter modulus m: ", min_val=2)
            inv = mod_inverse(a, m)
            if inv is not None:
                print(f"[+] Modular inverse: ({a}^-1) mod {m} = {inv}")
                print(f"    Verification  : ({a} * {inv}) % {m} = {(a * inv) % m}")
            else:
                print(f"[!] No modular inverse exists: GCD({a}, {m}) != 1.")
        elif choice == "6":
            base = get_int("Enter base a: ")
            exp = get_int("Enter exponent b: ", min_val=0)
            mod = get_int("Enter modulus m: ", min_val=1)
            print(f"[+] ({base}^{exp}) mod {mod} = {power_mod(base, exp, mod)}")
        elif choice == "7":
            n = get_int("Enter integer n (> 0): ", min_val=1)
            print(f"[+] Euler's Totient phi({n}) = {euler_totient(n)}")
        elif choice == "8":
            n = get_int("Enter non-negative integer: ", min_val=0)
            print(f"[+] Integer sqrt({n}) = {int_sqrt(n)}")
            print(f"[+] Smallest non-trivial divisor = {smallest_divisor(n)}")
        elif choice == "0":
            break


def run_ciphers_menu():
    """Sub-menu handler for Classical Cryptography."""
    while True:
        print("\n" + "-" * 40)
        print("  MODULE 2: CLASSICAL CRYPTOGRAPHY")
        print("-" * 40)
        print("1. Caesar Cipher Encrypt")
        print("2. Caesar Cipher Decrypt")
        print("3. Affine Cipher Encrypt")
        print("4. Affine Cipher Decrypt")
        print("5. Atbash Cipher (Symmetric)")
        print("0. Back to Main Menu")

        choice = get_choice("\nSelect an operation (0-5): ", {str(i) for i in range(6)})

        if choice == "1":
            text = get_string("Enter plaintext: ")
            shift = get_int("Enter shift value: ")
            print(f"[+] Ciphertext: {caesar_cipher(text, shift)}")
        elif choice == "2":
            text = get_string("Enter ciphertext: ")
            shift = get_int("Enter shift value: ")
            print(f"[+] Plaintext : {caesar_cipher(text, shift, decrypt=True)}")
        elif choice == "3":
            text = get_string("Enter plaintext: ")
            a = get_int("Enter multiplier key 'a' (must be coprime with 26): ")
            b = get_int("Enter additive key 'b': ")
            try:
                print(f"[+] Ciphertext: {affine_encrypt(text, a, b)}")
            except ValueError as e:
                print(f"[!] Error: {e}")
        elif choice == "4":
            text = get_string("Enter ciphertext: ")
            a = get_int("Enter multiplier key 'a' (must be coprime with 26): ")
            b = get_int("Enter additive key 'b': ")
            try:
                print(f"[+] Plaintext : {affine_decrypt(text, a, b)}")
            except ValueError as e:
                print(f"[!] Error: {e}")
        elif choice == "5":
            text = get_string("Enter text: ")
            print(f"[+] Transformed: {atbash_cipher(text)}")
        elif choice == "0":
            break


def run_conversions_menu():
    """Sub-menu handler for Base Conversions and Array Techniques."""
    while True:
        print("\n" + "-" * 40)
        print("  MODULE 3: CONVERSIONS & ARRAY TECHNIQUES")
        print("-" * 40)
        print("1. Decimal to Arbitrary Base (2 to 16)")
        print("2. Arbitrary Base (2 to 16) to Decimal")
        print("3. Text to ASCII Array & Reverse Reconstruction")
        print("4. Array Partitioning around Threshold")
        print("5. Remove Duplicates & K-th Smallest Element")
        print("0. Back to Main Menu")

        choice = get_choice("\nSelect an operation (0-5): ", {str(i) for i in range(6)})

        if choice == "1":
            num = get_int("Enter decimal integer: ")
            base = get_int("Enter target base (2-16): ", min_val=2, max_val=16)
            print(f"[+] Base {base} representation: {decimal_to_base(num, base)}")
        elif choice == "2":
            val_str = get_string("Enter numeric string: ")
            base = get_int("Enter source base (2-16): ", min_val=2, max_val=16)
            try:
                print(f"[+] Decimal equivalent: {base_to_decimal(val_str, base)}")
            except ValueError as e:
                print(f"[!] Error: {e}")
        elif choice == "3":
            text = get_string("Enter text string: ")
            ascii_arr = char_to_ascii(text)
            print(f"[+] ASCII Array: {ascii_arr}")
            print(f"[+] Reconstructed text: {ascii_to_char(ascii_arr)}")
            print(f"[+] Reversed ASCII Array: {reverse_array(ascii_arr)}")
        elif choice == "4":
            raw_input = get_string("Enter comma-separated integers: ")
            try:
                arr = [int(item.strip()) for item in raw_input.split(",") if item.strip()]
                pivot = get_int("Enter pivot threshold: ")
                lesser, geq = partition_array(arr, pivot)
                print(f"[+] Elements < {pivot} : {lesser}")
                print(f"[+] Elements >= {pivot}: {geq}")
            except ValueError:
                print("[!] Error: Malformed integer list provided.")
        elif choice == "5":
            raw_input = get_string("Enter comma-separated integers: ")
            try:
                arr = [int(item.strip()) for item in raw_input.split(",") if item.strip()]
                deduped = remove_duplicates(arr)
                print(f"[+] Array with duplicates removed: {deduped}")
                k = get_int(f"Enter k (1 to {len(deduped)}): ", min_val=1, max_val=len(deduped))
                print(f"[+] {k}-th smallest element: {find_kth_smallest(deduped, k)}")
            except (ValueError, IndexError) as e:
                print(f"[!] Error: {e}")
        elif choice == "0":
            break


def run_rsa_menu():
    """Sub-menu handler for Asymmetric RSA Keygen, Encryption & Decryption."""
    print("\n" + "-" * 40)
    print("  MODULE 4: ASYMMETRIC RSA ENGINE")
    print("-" * 40)
    print("Requires two distinct prime numbers (p and q).")
    p = get_int("Enter prime p (e.g., 61): ", min_val=2)
    q = get_int("Enter prime q (e.g., 53): ", min_val=2)

    try:
        rsa = RSASystem(p, q)
    except ValueError as e:
        print(f"[!] Initialization Failure: {e}")
        return

    print("\n[+] RSA Engine Initialized Successfully:")
    print(f"    Modulus n = p * q        : {rsa.n}")
    print(f"    Totient phi(n) = (p-1)*(q-1): {rsa.phi}")
    print(f"    Public Key (e, n)       : {rsa.public_key}")
    print(f"    Private Key (d, n)      : {rsa.private_key}")

    msg = get_string("\nEnter plaintext message to encrypt: ")
    try:
        cipher_blocks = rsa.encrypt_text(msg)
        print(f"[+] Encrypted Cipher Blocks: {cipher_blocks}")
        decrypted_text = rsa.decrypt_text(cipher_blocks)
        print(f"[+] Decrypted Plaintext    : '{decrypted_text}'")
        assert decrypted_text == msg
        print("[+] Verification Check     : SUCCESS (Decrypted matches input)")
    except ValueError as e:
        print(f"[!] Cryptographic Failure: {e}")


def main():
    """Primary Controller Loop."""
    while True:
        print("\n" + "=" * 50)
        print("    DISCRETE CRYPTOGRAPHY & NUMBER THEORY CLI    ")
        print("         CSE1021 Core Concept Showcase          ")
        print("=" * 50)
        print("1. Number Theory & Factoring Tools")
        print("2. Classical Substitution Ciphers")
        print("3. Data Conversions & Array Techniques")
        print("4. Asymmetric RSA Cryptosystem")
        print("0. Exit Application")

        selection = get_choice("\nEnter your selection (0-4): ", {"0", "1", "2", "3", "4"})

        if selection == "1":
            run_math_menu()
        elif selection == "2":
            run_ciphers_menu()
        elif selection == "3":
            run_conversions_menu()
        elif selection == "4":
            run_rsa_menu()
        elif selection == "0":
            print("\nShutting down CryptoCLI Engine. Goodbye!")
            break


if __name__ == "__main__":
    main()