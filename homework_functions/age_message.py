def age_message(age):
    if age < 18:
        return "Вы еще молоды!"
    elif age < 60:
        return "Вы в расцвете сил!"
    else:
        return "Вы мудры и опытны!"

print(age_message(30))