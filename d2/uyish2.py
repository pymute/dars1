def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
f = fibonacci()
for i in range(20):
    print(next(f))
