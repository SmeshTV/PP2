import mymodule

mymodule.greeting("Арман")


import mymodule

print(mymodule.person1["name"])  # Вывод: John


import mymodule as mx

mx.greeting("Арман")


import mymodule
print(dir(mymodule))


from mymodule import person1

print(person1["age"])  # Вывод: 36
