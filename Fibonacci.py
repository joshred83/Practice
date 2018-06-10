from time import localtime, strftime


def fibonacci(n):
    a, b, counter = 0, 1, 0
    while True:
        if counter > n: return
        yield a
        a, b = b, a + b
        counter += 1


f = fibonacci(10000)

for i, f in enumerate(f):
    if i == 1:
        print(strftime('%H:%M:%S', localtime()))
    elif i % 1000 == 0:
        print(strftime('%H:%M:%S', localtime()))

    print('{:>10}: {}'.format(i, f))
