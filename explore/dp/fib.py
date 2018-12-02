f = [0,1]

def fib(n):
    for i in range(2, n + 1):
        f.append(f[i - 1] + f[i - 2])
    return f[n]

def fib2(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib2(n - 1) + fib2(n - 2)


print(fib(100))

print(fib2(30))