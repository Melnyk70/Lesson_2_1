# Мельник Ігор - ДЗ 2.1. Виведення числа в стовпчик
user_input = input("Введіть чотирьохзначне ціле додатне число: ")  # Запит на ввід числа
# print(type(user_input))  # <class 'str'>
# print(user_input / 2)  # TypeError
number = int(user_input)
print("Вивід цифр числа по рядках:")  # число
print(number // 1000)  # 1 цифра
print(number % 1000 // 100)  # 2 цифра
print(number % 100 // 10)  # 3 цифра
print(number % 10)  # 4 цифра
