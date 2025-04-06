def check_string_length(string, length):
    if len(string) >= length:
        return "Длина строки достаточная"
    else:
        return "Строка слишком короткая"

# Пример использования:
result = check_string_length("Python", 5)
print(result)