from aes_gcm import aes_gcm_demo
from aes_cbc_hmac import aes_cbc_demo
from des3 import des3_demo
from rsa import rsa_demo
from hash_sha256 import hash_demo


def menu():
    print("\n===== 加密演算法示範主選單 =====")
    print("1. AES-GCM")
    print("2. AES-CBC + HMAC")
    print("3. TripleDES")
    print("4. RSA")
    print("5. SHA256 Hash + Salt")
    print("0. 離開")


if __name__ == "__main__":
    while True:
        menu()
        choice = input("請選擇要執行的演算法: ")

        if choice == "1":
            aes_gcm_demo()
        elif choice == "2":
            aes_cbc_demo()
        elif choice == "3":
            des3_demo()
        elif choice == "4":
            rsa_demo()
        elif choice == "5":
            hash_demo()
        elif choice == "0":
            print("\nEND!")
            break
        else:
            print("請輸入有效選項！")