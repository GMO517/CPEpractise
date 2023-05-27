def f(n):
    s = 0
    while n > 0:
        s = s+n % 10
        n = n//10
    return s


while True:
    n = int(input())
    if n == 0:
        break
    while f(n) > 9:
        n = f(n)
    print(f(n))
