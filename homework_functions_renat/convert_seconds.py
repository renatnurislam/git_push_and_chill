def convert_seconds(seconds):
    minutes = seconds // 60
    remaining_seconds = seconds % 60
    return f"{minutes} минут(ы) и {remaining_seconds} секунд(ы)"

print(convert_seconds(135))
