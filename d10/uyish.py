def palindromes():
    num = 0
    while True:
        if str(num) == str(num)[::-1]:
            yield num
        num += 1
