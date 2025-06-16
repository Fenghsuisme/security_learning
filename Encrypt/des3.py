import os
from base64 import b64encode, b64decode
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding


def des3_demo():
    print("\n--- TripleDES (3DES) 加密與解密示範 ---")

    # 1. 使用者輸入明文
    plaintext = input("請輸入要加密的文字: ").encode("utf-8")

    # 2. 產生 3DES 金鑰（24 bytes）與 IV（8 bytes）
    key = os.urandom(24)   # 3DES 要求 192 bits（24 bytes）
    iv = os.urandom(8)     # DES 區塊大小為 64 bits（8 bytes）

    # 3. 補 padding（3DES 是區塊加密，需要補齊）
    padder = padding.PKCS7(64).padder()  # DES 區塊大小 = 64 bits
    padded_data = padder.update(plaintext) + padder.finalize()

    # 4. 加密
    cipher = Cipher(algorithms.TripleDES(key), modes.CBC(iv))
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()

    # 5. 輸出加密資料（轉成 base64）
    print("\n金鑰 (hex):", key.hex())
    print("IV (hex):", iv.hex())
    print("密文 (base64):", b64encode(ciphertext).decode())

    # 6. 解密流程
    decryptor = cipher.decryptor()
    padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()
    unpadder = padding.PKCS7(64).unpadder()
    plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()

    print("✅ 解密成功，原文為:", plaintext.decode("utf-8"))