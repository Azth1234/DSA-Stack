def karatsuba(x, y):

    # Base case
    if x < 10 or y < 10:
        return x * y

    n = max(len(str(x)), len(str(y)))
    m = n // 2

    # Split numbers
    a = x // 10**m
    b = x % 10**m
    c = y // 10**m
    d = y % 10**m

    # Recursive calls
    p1 = karatsuba(a, c)
    p2 = karatsuba(b, d)
    p3 = karatsuba((b + a), (d + c))
    

    return (p1 * 10**(2*m)) + ((p3 - p2 - p1) * 10**m) + p2


x = 1234
y = 5678

print("Multiplication:", karatsuba(x, y))