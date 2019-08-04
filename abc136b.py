n = int(input())
if 1 <= n and n <= 9:
    print(n)
elif 10 <= n and n <= 99:
    print(9)
elif 100 <= n and n <= 999:
    print(9+n-99)
elif 1000 <= n and n <= 9999:
    print(9+999-99)
elif 10000 <= n and n <= 99999:
    print(9+999-99+n-9999)
elif 100000 <= n and n <= 999999:
    print(9+999-99+99999-9999)