# CryptographCLI: Discrete Mathematics & Cryptography Engine

A modular, dependency-free command-line application that demonstrates fundamental algorithms, factoring methods, array techniques, and asymmetric cryptography[cite: 1, 2, 4]. Developed in alignment with the **CSE1021 Introduction to Problem Solving and Programming** curriculum[cite: 1].

---

## 1. Features
- **Module 1: Number Theory & Factoring Tools**
  - Euclidean Greatest Common Divisor (GCD) and Least Common Multiple (LCM)[cite: 1].
  - Optimized Primality Checking ($O(\sqrt{n})$) and Prime Generation[cite: 1].
  - Canonical Prime Factorization and Smallest Divisor Search[cite: 1].
  - Extended Euclidean Algorithm for Modular Multiplicative Inverses[cite: 1].
  - Fast Binary Exponentiation (Repeated Squaring) for $a^b \pmod m$[cite: 1].
  - Euler's Totient Function $\phi(n)$ via prime factorization[cite: 1].
- **Module 2: Classical Substitution Ciphers**
  - Caesar Cipher with configurable shift bounds[cite: 1].
  - Affine Cipher ($E(x) = (ax + b) \pmod{26}$) with coprimality validation[cite: 1].
  - Atbash Symmetric Alphabet Transformation[cite: 1].
- **Module 3: Conversions & Array Techniques**[cite: 1, 2]
  - Multi-base numeric conversions (Decimal to Base 2–16 and inverse)[cite: 1].
  - Text-to-ASCII integer mappings and reversal algorithms[cite: 1].
  - Array partitioning based on dynamic pivot thresholds[cite: 1].
  - In-place duplicate removal and $k$-th smallest element search[cite: 1].
- **Module 4: Asymmetric RSA Cryptosystem**
  - End-to-end key generation from twin primes $(p, q)$[cite: 1].
  - Public Key $(e, n)$ and Private Key $(d, n)$ derivation[cite: 1].
  - Text-to-block encryption and block-to-text decryption verification[cite: 1].

---

## 2. Technologies & Architecture
- **Language:** Pure Python (Compatible with Python 3.10+)[cite: 2, 4].
- **Dependencies:** None (Relies strictly on standard language features)[cite: 2, 4].
- **Design Pattern:** Modular Layered Architecture separating algorithmic logic (`crypto_core`) from interaction handlers (`validator.py`, `main.py`).

---

## 3. Installation & Execution

### Prerequisites
Ensure Python 3.10 or higher is installed:
```bash
python3 --version
