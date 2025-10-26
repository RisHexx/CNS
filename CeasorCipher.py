#ord() → converts a character to its Unicode (integer) code point
#chr() → converts a Unicode (integer) code point back to a character

def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():  # Encrypt only alphabets
            base = ord('A') if char.isupper() else ord('a')


            # Shift character and wrap around using modulo
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char  # Keep spaces and other chars unchanged
    return result


def caesar_cipher_decrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():  # Encrypt only alphabets
            base = ord('A') if char.isupper() else ord('a')
            # Shift character and wrap around using modulo
            result += chr((ord(char) - base - shift) % 26 + base)
            #                               ^ part only we are just subtracting the shift
        else:
            result += char  # Keep spaces and other chars unchanged
    return result
# Example usage

text = "XIE IS BEST"
shift = 3  # You can change the shift value
encrypted_text = caesar_cipher(text, shift)
decrpyed_text = caesar_cipher_decrypt( "aLH LV EHVW" , shift)
print("Original Text:", text)
print("Encrypted Text:", encrypted_text)
print("Decrypted Text:", decrpyed_text)
