def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    offset_ascii_upper = 65
    offset_ascii_lower = 97
    for i in plaintext:
        if i.isalpha():
            if i.islower():
                ciphertext += chr((ord(i) - offset_ascii_lower + shift)%26+offset_ascii_lower)
            else:
                ciphertext += chr((ord(i) - offset_ascii_upper + shift)%26+offset_ascii_upper)
        else:
            ciphertext += i
    return ciphertext



def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    offset_ascii_upper = 65
    offset_ascii_lower = 97
    for i in ciphertext:
        if i.isalpha():
            if i.islower():
                plaintext += chr((ord(i) - offset_ascii_lower - shift) % 26 + offset_ascii_lower)
            else:
                plaintext += chr((ord(i) - offset_ascii_upper - shift) % 26 + offset_ascii_upper)
        else:
            plaintext += i
    return plaintext