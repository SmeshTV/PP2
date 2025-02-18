import re

with open(r"C:\Users\Arman\Desktop\PP2\Lab 5\regex\row.txt", encoding="utf-8") as f:
    text = f.read()


def camel_to_snake(s):
    return re.sub(r"([A-Z])", r"_\1", s).lower().lstrip("_")

matches = re.findall(r"\b[A-Z][a-zA-Z]*\b", text)
converted = [camel_to_snake(m) for m in matches]
print(converted)
