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


text = "aLH LV EHVW"

for i in range(1,27):
    dec = caesar_cipher_decrypt(text , i)
    print(dec)
