import os

filename = r"C:\Users\Arman\Desktop\PP2\Lab 6\dir-and-files\copy_example.txt"

if os.path.exists(filename):
    os.remove(filename)
    print(f"{filename} deleted")