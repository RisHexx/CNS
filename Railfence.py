cipher_text = ""
def railfence(plain_text,key):
    if key == 2:
        return plain_text[::2] + plain_text[1::2]
    else:
        return "Invalid Key"


def railfence_decrypt(cipher_text):
    block1 = cipher_text[:5:]
    block2 = cipher_text[5::]
    decrypted_text = ""
    for i in range(len(block2)):
        decrypted_text = decrypted_text + block1[i] + block2[i]
    if len(block1) > len(block2):
        decrypted_text = decrypted_text + block1[-1]
    return decrypted_text


plain_text = "XIEISBEST"
# encrypted_text = railfence(plain_text , 2)
# product_text = railfence(encrypted_text,2)
# print(plain_text)
# print(product_text)

encrypted_message = "xeietisbs"
decrypt = railfence_decrypt(encrypted_message)
# product_decrypt = railfence_decrypt(decrypt)
print(decrypt)