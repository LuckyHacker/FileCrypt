import hashlib
import sys
import os
from Crypto import Random
from Crypto.Cipher import AES
from lib.crypt import crypt

class AESCipher:

    def __init__(self, key, src_filepath, dst_filepath):
        self.src_filepath = src_filepath
        self.dst_filepath = dst_filepath
        self.bs = 32
        self.key = hashlib.sha256(key.encode()).digest()

    def encrypt(self):
        with open(self.src_filepath, "rb") as f:
            raw = str(self._pad(f.read()), "latin-1")
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        with open(self.dst_filepath, "wb") as f:
            f.write(iv + cipher.encrypt(raw))

    def decrypt(self):
        with open(self.src_filepath, "rb") as f:
            enc = str(f.read(), "latin-1")
        iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        with open(self.dst_filepath, "wb") as f:
            f.write(self._unpad(cipher.decrypt(enc[AES.block_size:])).decode('latin-1'))

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s)-1:])]


class CryptCipher:

    def __init__(self, key, src_filepath, dst_filepath):
        self.src_filepath = src_filepath
        self.dst_filepath = dst_filepath
        self.key = key

    def encrypt(self):
        crypt.XORFile(self.src_filepath, self.key).encrypt(self.dst_filepath)

    def decrypt(self):
        crypt.XORFile(self.src_filepath, self.key).decrypt(self.dst_filepath)
