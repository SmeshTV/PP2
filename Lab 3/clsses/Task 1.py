class MyClass:
    def getString(self):
        self.string = input("Введите строку: ")

    def printString(self):
        print(self.string.upper())

obj = MyClass()
obj.getString()
obj.printString()
