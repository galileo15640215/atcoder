n = int(input())
s = input()
cnt = 0
for i in range(0, n, 1):
    for j in range(i+1, n, 1):
        for k in range(j+1, n, 1):
            if s[i] != s[j] and s[i] != s[k] and s[j] != s[k] and j-i != k-j:
                cnt += 1
print(cnt)