def is_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return "Треугольник существует"
    else:
        return "Треугольник не существует"

print(is_triangle(3, 4, 5))
