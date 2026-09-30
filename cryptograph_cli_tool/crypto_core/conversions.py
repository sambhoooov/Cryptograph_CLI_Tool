"""
Fundamental transformations and array operations covering CSE1021 Units 3 and 5:
Base conversions, Character-to-Number conversion, Array reversals, and Partitioning.
"""

def char_to_ascii(text: str) -> list[int]:
    """Converts a text string to an array of ASCII integer ordinals."""
    return [ord(ch) for ch in text]


def ascii_to_char(arr: list[int]) -> str:
    """Reconstructs a text string from an array of ASCII ordinals."""
    return "".join(chr(val) for val in arr)


def decimal_to_base(n: int, base: int) -> str:
    """
    Converts a non-negative decimal integer into an arbitrary base representation (2 to 16).
    """
    if not (2 <= base <= 16):
        raise ValueError("Base must be between 2 and 16 inclusive.")
    if n == 0:
        return "0"
    
    digits = "0123456789ABCDEF"
    result = []
    temp = abs(n)
    while temp > 0:
        result.append(digits[temp % base])
        temp //= base
    
    result.reverse()
    prefix = "-" if n < 0 else ""
    return prefix + "".join(result)


def base_to_decimal(val_str: str, base: int) -> int:
    """
    Parses a string in base (2 to 16) into its decimal integer value.
    """
    if not (2 <= base <= 16):
        raise ValueError("Base must be between 2 and 16 inclusive.")
    digits = "0123456789ABCDEF"
    val_str = val_str.strip().upper()
    is_neg = val_str.startswith("-")
    if is_neg:
        val_str = val_str[1:]
    
    total = 0
    for char in val_str:
        digit_val = digits.find(char)
        if digit_val == -1 or digit_val >= base:
            raise ValueError(f"Invalid character '{char}' for base {base}.")
        total = total * base + digit_val
        
    return -total if is_neg else total


def reverse_array(arr: list) -> list:
    """Reverses an array without external helper libraries."""
    reversed_list = []
    for i in range(len(arr) - 1, -1, -1):
        reversed_list.append(arr[i])
    return reversed_list


def partition_array(arr: list[int], pivot: int) -> tuple[list[int], list[int]]:
    """
    Partitions an array into two lists: elements < pivot and elements >= pivot.
    """
    lesser = []
    greater_or_equal = []
    for item in arr:
        if item < pivot:
            lesser.append(item)
        else:
            greater_or_equal.append(item)
    return lesser, greater_or_equal


def remove_duplicates(arr: list) -> list:
    """
    Removes duplicate values from an array while preserving original order.
    """
    seen = set()
    deduped = []
    for item in arr:
        if item not in seen:
            seen.add(item)
            deduped.append(item)
    return deduped


def find_kth_smallest(arr: list[int], k: int) -> int:
    """
    Finds the k-th smallest element (1-indexed) in an integer array.
    """
    if not (1 <= k <= len(arr)):
        raise IndexError("k is out of array bounds.")
    sorted_copy = sorted(arr)
    return sorted_copy[k - 1]