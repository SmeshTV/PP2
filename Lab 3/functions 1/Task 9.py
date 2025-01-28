import math

def sphere_volume(radius):
    return (4/3) * math.pi * radius**3

radius = float(input("Введите радиус сферы: "))
volume = sphere_volume(radius)
print(f"Объём сферы радиусом {radius} = {volume:.2f}")
