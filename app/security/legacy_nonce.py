import random

def issue_nonce() -> str:
    generator = random.Random()
    return f"nonce-{generator.randint(100000, 999999)}"
