from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding


def rsa_demo():
    print("\n--- RSA 非對稱加密與解密示範 ---")

    # 1. 產生 RSA 金鑰對（2048 bits）
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()

    # 2. 顯示金鑰資訊（PEM 格式）
    pem_private = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )
    pem_public = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    print("私鑰 PEM:")
    print(pem_private.decode())
    print("公鑰 PEM:")
    print(pem_public.decode())

    # 3. 加密（使用公鑰）
    plaintext = input("請輸入要加密的文字: ").encode("utf-8")
    ciphertext = public_key.encrypt(
        plaintext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    print("\n加密後密文（hex）:", ciphertext.hex())

    # 4. 解密（使用私鑰）
    decrypted = private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    print("✅ 解密成功，原文為:", decrypted.decode("utf-8"))