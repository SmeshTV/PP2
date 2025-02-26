import os

path = r"C:\Users\Arman\Desktop\PP2\Lab 6\dir-and-files\example.txt"

if os.path.exists(path):
    print("Path exists")
    print("Readable:", os.access(path, os.R_OK))
    print("Writable:", os.access(path, os.W_OK))
    print("Executable:", os.access(path, os.X_OK))
else:
    print("Path does not exist")