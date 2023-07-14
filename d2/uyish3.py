def palindrome_generator():
    num = 11
    while True:
        if str(num) == str(num)[::-1]:
            yield num
        num += 1

my_gen = palindrome_generator()

for i in range(10):
    print(next(my_gen))