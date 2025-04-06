def count_vowels(string):
    vowels = "aeiou"
    count = 0
    for char in string.lower():
        if char in vowels:
            count += 1
    return count

print("Гласных в 'Hello World':", count_vowels("Hello World"))
