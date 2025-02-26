filename = r"C:\Users\Arman\Desktop\PP2\Lab 6\dir-and-files\output.txt"

data = ["apple", "banana", "cherry"]

with open(filename, "w") as file:
    for item in data:
        file.write(item + "\n")