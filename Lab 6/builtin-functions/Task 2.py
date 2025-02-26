text = "Hello World!"
upper_count = sum(1 for c in text if c.isupper())
lower_count = sum(1 for c in text if c.islower())
print("Uppercase:", upper_count, "Lowercase:", lower_count)
