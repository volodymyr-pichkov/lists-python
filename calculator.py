num1 = float(input("Введіть перше число: "))
num2 = float(input("Введіть друге число: "))
operation = input("Введіть дію (+, -, *, /): ")

if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Помилка! Ділення на нуль неможливе."
else:
    result = "Невідома операція"

print("Результат:", result)
