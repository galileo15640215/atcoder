c = input()
cnt = len(c)
for i in range(len(c)):
    if c[i] == '0':
        cnt -= 1
print(cnt-1)
