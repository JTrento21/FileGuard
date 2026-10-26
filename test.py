from src.backend.scan import *
from src.backend.hash import *

s = scan(r"C:\Users\Joaot\OneDrive\Desktop\FileGuard\test_files")

print(s)

for file in s['Files']:
    print(hash_file_sha256(file))
    