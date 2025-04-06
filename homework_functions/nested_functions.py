def outer(a, b):
    def inner(x, y):
        return x + y
    return inner(a, b) * 2

print(outer(3, 4))
