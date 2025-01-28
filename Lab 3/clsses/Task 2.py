class Shape:
    def __init__(self):
        self.area = 0

    def area(self):
        return self.area


class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length

    def area(self):
        return self.length ** 2


shape = Shape()
print("Площадь Shape по умолчанию:", shape.area)

square = Square(4)
print("Площадь квадрата:", square.area())
