# Queens College
# Internet And Web Technologies (CSCI 355)
# Winter 2024
# Assignment #8B- Classic and Modern Cryptography
# Frederick Burke
# I did this assignment along with the class
from numpy import random
import numpy as np
import rsa
alphabet = [chr(ord('A') + i) for i in range(26)]


def sub_cipher(alphabet):
    return random.permutation(alphabet)


def encrypt(text, cipher):
    return ''.join([cipher[ord(c) - 65] for c in text])


def decrypt(text, cipher):
    return ''.join([chr(cipher.index(c)+65) for c in text])

def encrypt_rsa(cipher, pub_key):
    cipher = cipher.encode('utf-8')
    encrypted_cipher = rsa.encrypt(cipher, pub_key)
    return encrypted_cipher


def get_keys():
    return rsa.newkeys(2048)


def decrypt_rsa(encrypted_cipher, priv_key):
    return rsa.decrypt(encrypted_cipher, priv_key).decode('utf-8')


def read_file(file_name):
    with open(file_name) as f:
        return f.read()


def write_file(file_name, text):
    with open(file_name, "w") as f:
        f.write(text)


def main():
    text = read_file('Assignment8d.txt')
    alphabet = [chr(ord('A')+i) for i in range(26)]
    cipher = sub_cipher(alphabet)
    encrypted_text = encrypt(text, cipher)
    write_file('Assignment8e2.txt', encrypted_text)
    decrypted_text = decrypt(encrypted_text, cipher.tolist())
    print(decrypted_text)
    pub_key, priv_key = get_keys()
    encrypted_cipher = encrypt_rsa(', '.join(cipher.tolist()), pub_key)
    print("This is the encrypted cipher", encrypted_cipher)
    decrypted_cipher = decrypt_rsa(encrypted_cipher, priv_key)
    print("This is the decrypted cipher", decrypted_cipher)



if __name__ == '__main__':
    main()
