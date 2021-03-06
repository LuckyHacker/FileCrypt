import hashlib
import base64
from Crypto import Random
from Crypto.Cipher import AES
from lib.crypt import crypt
from Crypto.Cipher import Blowfish


class AESCipher:

    def __init__(self, key, src_filepath, dst_filepath):
        self.src_filepath = src_filepath
        self.dst_filepath = dst_filepath
        self.bs = AES.block_size
        self.key = hashlib.sha256(key.encode()).digest()

    def encrypt(self):
        with open(self.src_filepath, "rb") as f:
            plaintext_base64 = base64.b64encode(f.read())
            raw = self._pad(str(plaintext_base64, "latin-1"))
        iv = Random.new().read(self.bs)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        with open(self.dst_filepath, "wb") as f:
            f.write(iv + cipher.encrypt(bytes(raw, "latin-1")))

    def decrypt(self):
        with open(self.src_filepath, "rb") as f:
            enc = f.read()
        iv = enc[:self.bs]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        with open(self.dst_filepath, "wb") as f:
            decrypted_base64 = cipher.decrypt(enc[self.bs:])
            f.write(base64.b64decode(bytes(self._unpad(str(decrypted_base64, "latin-1")), "latin-1")))

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


class BlowfishCipher:

    def __init__(self, key, src_filepath, dst_filepath):
        self.src_filepath = src_filepath
        self.dst_filepath = dst_filepath
        self.bs = Blowfish.block_size
        self.key = hashlib.sha256(key.encode()).digest()

    def encrypt(self):
        with open(self.src_filepath, "rb") as f:
            plaintext_base64 = base64.b64encode(f.read())
            raw = self._pad(str(plaintext_base64, "latin-1"))
        iv = Random.new().read(self.bs)
        cipher = Blowfish.new(self.key, Blowfish.MODE_CBC, iv)
        with open(self.dst_filepath, "wb") as f:
            f.write(iv + cipher.encrypt(bytes(raw, "latin-1")))

    def decrypt(self):
        with open(self.src_filepath, "rb") as f:
            enc = f.read()
        iv = enc[:self.bs]
        cipher = Blowfish.new(self.key, Blowfish.MODE_CBC, iv)
        with open(self.dst_filepath, "wb") as f:
            decrypted_base64 = cipher.decrypt(enc[self.bs:])
            f.write(base64.b64decode(bytes(self._unpad(str(decrypted_base64, "latin-1")), "latin-1")))

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s)-1:])]
