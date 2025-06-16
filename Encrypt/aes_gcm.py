import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM


def aes_gcm_demo():
    print("\n--- AES-GCM 加密與解密示範 ---")

    # 1. 使用者輸入
    plaintext = input("請輸入要加密的文字: ")

    # 2. 產生隨機金鑰（256 bit）和 nonce（初始化向量）
    key = AESGCM.generate_key(bit_length=256)
    nonce = os.urandom(12)  # GCM 模式要求 12 bytes 的 nonce

    # 3. 建立 AESGCM 物件並加密
    aesgcm = AESGCM(key)
    ciphertext = aesgcm.encrypt(nonce, plaintext.encode("utf-8"), None)

    #---- 檢視 ----
    print(f"\n密文（hex）: {ciphertext.hex()}")
    print(f"金鑰（hex）: {key.hex()}")
    print(f"Nonce（hex）: {nonce.hex()}")

    # 4. 解密
    try:
        decrypted = aesgcm.decrypt(nonce, ciphertext, None).decode("utf-8")
        print(f"\n✅ 解密成功，原文是: {decrypted}")
    except Exception as e:
        print(f"\n❌ 解密失敗：{e}") 