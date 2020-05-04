n = int(input())
a = []
for i in range(n):
    s = int(input())
    a.append(s)
a.sort()
i = 0
cnt = 0
while i < n:
    j = i+1
    chk = 1
    if j >= n:
        cnt += 1 
        break
    while a[i] == a[j]:
        chk += 1
        j += 1
        if j >= n:
            break
    if chk%2 == 1:
        cnt += 1 
    i = j
print(cnt)