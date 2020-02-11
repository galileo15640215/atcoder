a, b = map(int, input().split())
a, b = min(a, b), max(a, b)
for i in range(b):
    print(a, end="")
print()