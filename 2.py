# Введення двох дійсних чисел
a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))

# Перевірка та заміна значень
if a < b:
    a, b = 0, 1
else:
    a, b = 1, 0

# Виведення результату
print(f"Перше число: {a}")
print(f"Друге число: {b}")
