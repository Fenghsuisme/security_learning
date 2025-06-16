import os, hashlib, hmac
from base64 import b64encode
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding


def aes_cbc_demo():
    print("\n--- AES-CBC + HMAC 加密與驗證示範 ---")

    # 使用者輸入明文
    plaintext = input("請輸入要加密的文字: ").encode("utf-8")

    # 金鑰產生：AES 與 HMAC 各 256-bit（32 bytes）
    aes_key = os.urandom(32)
    hmac_key = os.urandom(32)
    iv = os.urandom(16)  # CBC 模式的 IV 固定為 16 bytes

    # 明文補齊（PKCS7 padding）
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(plaintext) + padder.finalize()

    # 使用 AES-CBC 模式進行加密
    cipher = Cipher(algorithms.AES(aes_key), modes.CBC(iv))
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()

    # 建立 HMAC（以 iv + ciphertext 為驗證對象）
    tag = hmac.new(hmac_key, iv + ciphertext, hashlib.sha256).digest()

    # ---- 檢視 ----
    print("AES 金鑰（hex）:", aes_key.hex())
    print("HMAC 金鑰（hex）:", hmac_key.hex())
    print("IV（hex）:", iv.hex())
    print("密文（base64）:", b64encode(ciphertext).decode())
    print("HMAC 標籤（hex）:", tag.hex())

    # 解密流程
    print("\n--- 解密階段模擬 ---")
    try:
        # 驗證 HMAC
        verify_tag = hmac.new(hmac_key, iv + ciphertext, hashlib.sha256).digest()
        if not hmac.compare_digest(tag, verify_tag):
            raise ValueError("HMAC 驗證失敗！資料可能被竄改。")

        # 解密並去除 padding
        decryptor = cipher.decryptor()
        padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()
        unpadder = padding.PKCS7(128).unpadder()
        plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()

        print("✅ 解密成功，原文為：", plaintext.decode())
    except Exception as e:
        print("❌ 解密失敗：", e)