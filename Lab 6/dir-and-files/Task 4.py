filename = r"C:\Users\Arman\Desktop\PP2\Lab 6\dir-and-files\example.txt"

with open(filename, "r") as file:
    print("Number of lines:", sum(1 for line in file))
