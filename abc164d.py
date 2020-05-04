s = input()
cnt = 0
for i in range(len(s)-3):
    for j in range(i+4, len(s)):
        tmp = int(s[i:j+1])
        if tmp%2019 == 0:
            cnt += 1
print(cnt)