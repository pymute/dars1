def primes():
    num = 2
    primes_list = []
    while True:
        for prime in primes_list:
            if num % prime == 0:
                break
        else:
            primes_list.append(num)
            yield num
        num += 1
