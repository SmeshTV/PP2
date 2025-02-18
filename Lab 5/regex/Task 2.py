import re

with open(r"C:\Users\Arman\Desktop\PP2\Lab 5\regex\row.txt", encoding="utf-8") as f:
    text = f.read()

matches = re.findall(r"a[b]{2,3}", text)
print(matches)
