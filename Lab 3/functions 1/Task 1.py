def grams_to_ounces(grams):
    ounces = grams / 28.3495231
    return ounces

grams = float(input("Введите количество граммов: "))
ounces = grams_to_ounces(grams)
print(f"{grams} граммов = {ounces:.2f} унции")
