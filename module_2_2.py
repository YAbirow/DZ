# Ввод трех целых чисел
first = int(input("Введите первое число: "))
second = int(input("Введите второе число: "))
third = int(input("Введите третье число: "))

# Условная конструкция для проверки равенства чисел
if first == second == third:
    print(3)  # Все числа равны
elif first == second or second == third or first == third:
    print(2)  # Есть хотя бы 2 одинаковых числа
else:
    print(0)  # Все числа разные