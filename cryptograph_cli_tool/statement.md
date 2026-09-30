# Project Statement & Scope Specification

## 1. Problem Statement
Discrete mathematics, factoring methods, and modular arithmetic form the theoretical basis of modern data security. However, learners often experience a conceptual disconnect between theoretical algorithms (such as the Euclidean Algorithm, Extended GCD, modular exponentiation, and array partitioning) and their application in data protection. The **CryptoCLI Engine** addresses this gap by providing an offline, terminal-based software suite that demonstrates how number theory and array structures implement classical and modern cryptosystems[cite: 1, 4].

## 2. Scope of the Project
The software encompasses:
- Pure Python algorithmic implementations without external library dependencies.
- Discrete number-theoretic operations: Greatest Common Divisor, Least Common Multiple, Extended Euclidean modular inverse, Newton-Raphson integer square roots, and Euler's Totient function.
- Array and transformation techniques: Base conversion (bases 2 to 16), ASCII array transformations, array order reversal, array partitioning around a pivot, and duplicate removal.
- Cryptographic systems: Classical symmetric substitution ciphers (Caesar, Affine, Atbash) and asymmetric public-key cryptography (RSA keypair generation, block encryption, and decryption)[cite: 1, 2].

## 3. Target Users
- **Computer Science & Engineering Students:** Studying fundamental algorithms, complexity analysis, and modular arithmetic in CSE1021.
- **Academic Evaluators:** Requiring a modular, verifiable, zero-dependency codebase that demonstrates syllabus outcomes without relying on third-party black-box libraries[cite: 1, 2].
- **Security Enthusiasts:** Seeking an offline environment to trace how mathematical keys encrypt and decrypt textual data[cite: 2, 4].

## 4. High-Level Features
- **Deterministic Math Core:** Algorithmic solutions for primality verification ($O(\sqrt{n})$) and fast modular exponentiation ($O(\log b)$)[cite: 1].
- **Symmetric Cryptographic Suite:** Parameterized cipher execution with automatic key coprimality checks[cite: 1].
- **Complete RSA Engine:** Prime validation, Euler totient computation, private key derivation, and character-level block transformation[cite: 1].
- **Crash-Resilient Interface:** Modular input validation ensuring continuous CLI execution without uncaught runtime errors[cite: 2, 4].