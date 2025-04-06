def is_even(number):
    return "чётное" if number % 2 == 0 else "нечётное"

# Пример использования:
num = int(input("Введите число: "))
result = is_even(num)
print(f"Число {num} является {result}.")