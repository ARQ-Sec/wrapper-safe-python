import secrets

def random_or_not(value: bytes) -> str:
    return secrets.token_hex(16)
