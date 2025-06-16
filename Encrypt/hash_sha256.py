import hashlib, os
from base64 import b64encode


def hash_demo():
    print("\n--- SHA256 加鹽雜湊示範 ---")

    # 1. 使用者輸入密碼（明文）
    password = input("請輸入要加密儲存的密碼: ").encode("utf-8")

    # 2. 產生隨機 salt（加鹽防彩虹表）
    salt = os.urandom(16)

    # 3. 雜湊：SHA256(salt + password)
    hasher = hashlib.sha256()
    hasher.update(salt + password)
    hash_result = hasher.digest()

    print("\nSalt (hex):", salt.hex())
    print("雜湊值 (hex):", hash_result.hex())
    print("可儲存格式: [salt|hash] =", salt.hex() + ":" + hash_result.hex())

    # 4. 模擬登入驗證：重新輸入密碼比對
    print("\n--- 模擬登入驗證 ---")
    attempt = input("請輸入密碼驗證: ").encode("utf-8")
    hasher2 = hashlib.sha256()
    hasher2.update(salt + attempt)
    attempt_hash = hasher2.digest()

    if attempt_hash == hash_result:
        print("✅ 驗證成功，密碼正確！")
    else:
        print("❌ 驗證失敗，密碼錯誤！")
