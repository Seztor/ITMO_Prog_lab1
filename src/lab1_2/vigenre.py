from string import ascii_uppercase

def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    ciphertext = ""
    shift_code_arr = {let:ind for ind, let in enumerate(ascii_uppercase)}
    offset_ascii_upper = 65
    offset_ascii_lower = 97
    keyword_ind_current = 0

    for i in plaintext:
        shift = shift_code_arr[keyword[keyword_ind_current].upper()]
        if i.isalpha():
            if i.islower():
                ciphertext += chr((ord(i) - offset_ascii_lower + shift)
                                  % 26 + offset_ascii_lower)
            else:
                ciphertext += chr((ord(i) - offset_ascii_upper + shift)
                                  % 26 + offset_ascii_upper)
        else:
            ciphertext += i
        keyword_ind_current += 1
        if keyword_ind_current == len(keyword):
            keyword_ind_current = 0
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    plaintext = ""
    shift_code_arr = {let: ind for ind, let in enumerate(ascii_uppercase)}
    offset_ascii_upper = 65
    offset_ascii_lower = 97
    keyword_ind_current = 0

    for i in ciphertext:
        shift = shift_code_arr[keyword[keyword_ind_current].upper()]
        if i.isalpha():
            if i.islower():
                plaintext += chr((ord(i) - offset_ascii_lower - shift)
                                 % 26 + offset_ascii_lower)
            else:
                plaintext += chr((ord(i) - offset_ascii_upper - shift)
                                 % 26 + offset_ascii_upper)
        else:
            plaintext += i
        keyword_ind_current += 1
        if keyword_ind_current == len(keyword):
            keyword_ind_current = 0
    return plaintext