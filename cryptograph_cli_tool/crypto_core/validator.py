"""
Terminal input validation and sanitization module.
Ensures crash-resilient CLI operations under edge cases and invalid entries.
"""

def get_int(prompt: str, min_val: int | None = None, max_val: int | None = None) -> int:
    """
    Prompts the user repeatedly until a valid integer within boundaries is received.
    """
    while True:
        raw = input(prompt).strip()
        try:
            val = int(raw)
            if min_val is not None and val < min_val:
                print(f"[!] Input Error: Value must be >= {min_val}.")
                continue
            if max_val is not None and val > max_val:
                print(f"[!] Input Error: Value must be <= {max_val}.")
                continue
            return val
        except ValueError:
            print("[!] Format Error: Please enter a valid integer (e.g., 42, -7).")


def get_string(prompt: str, allow_empty: bool = False) -> str:
    """
    Prompts the user for a text string, re-prompting if left empty when prohibited.
    """
    while True:
        raw = input(prompt)
        if not allow_empty and len(raw.strip()) == 0:
            print("[!] Input Error: Text entry cannot be blank.")
            continue
        return raw


def get_choice(prompt: str, valid_options: set[str]) -> str:
    """
    Prompts the user until a selection within the allowed options set is entered.
    """
    while True:
        entry = input(prompt).strip()
        if entry in valid_options:
            return entry
        print(f"[!] Selection Error: Invalid choice '{entry}'. Valid options: {sorted(list(valid_options))}")
        