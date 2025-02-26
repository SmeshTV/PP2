import string
import os

directory = r"C:\Users\Arman\Desktop\PP2\Lab 6\dir-and-files"

for letter in string.ascii_uppercase:
    open(os.path.join(directory, f"{letter}.txt"), "w").close()