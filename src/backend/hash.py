import hashlib


def hash_sha256(file_path: str) -> str:
    with open(file_path, "rb") as f:
        digest = hashlib.file_digest(f, "sha256")
    return digest.hexdigest()

if __name__ == "__main__":
    print(hash_sha256(r"C:\Users\Joaot\OneDrive\Desktop\FileGuard\test_files\test_1"))

