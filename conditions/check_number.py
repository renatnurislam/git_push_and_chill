def check_number(number):
    if number > 0:
        if number % 2 == 0:
            return f"Число {number} положительное и чётное."
        else:
            return f"Число {number} положительное и нечётное."
    else:
        return f"Число {number} отрицательное."

# Пример использования:
num = int(input("Введите число: "))
result = check_number(num)
print(result)