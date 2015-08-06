def fib(limit):
    num1, num2 = 0, 1
    while num1 < limit:
        if not num1 % 2:
            yield num1
        num1, num2 = num2, num1 + num2

print(sum(fib(4000000)))