def check_grade(score):
    if score >= 90:
        return "Отлично"
    elif score >= 75:
        return "Хорошо"
    elif score >= 50:
        return "Удовлетворительно"
    else:
        return "Неудовлетворительно"

# Пример:
result = check_grade(85)
print(result)