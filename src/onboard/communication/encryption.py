"""
AES Encryption for Secure Telemetry and Commands
"""
from Crypto.Cipher import AES
import os

class Encryptor:
    def __init__(self, key):
        self.key = key

    def encrypt(self, plaintext):
        cipher = AES.new(self.key, AES.MODE_GCM)
        ciphertext, tag = cipher.encrypt_and_digest(plaintext)
        return cipher.nonce + tag + ciphertext

    def decrypt(self, enc_bytes):
        nonce = enc_bytes[:16]
        tag = enc_bytes[16:32]
        ciphertext = enc_bytes[32:]
        cipher = AES.new(self.key, AES.MODE_GCM, nonce=nonce)
        return cipher.decrypt_and_verify(ciphertext, tag)
