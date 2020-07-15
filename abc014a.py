a = int(input())
b = int(input())
tmp = b
for i in range(100):
    if a <= tmp:
        break
    tmp += b
print(tmp-a)