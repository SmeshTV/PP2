import re

with open(r"C:\Users\Arman\Desktop\PP2\Lab 5\regex\row.txt", encoding="utf-8") as f:
    text = f.read()


def snake_to_camel(s):
    return "".join(word.capitalize() for word in s.split("_"))

matches = re.findall(r"\b[a-z]+_[a-z_]+\b", text)
converted = [snake_to_camel(m) for m in matches]
print(converted)
