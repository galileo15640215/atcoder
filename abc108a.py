k = int(input())
cnt = 0
for i in range(1, k+1):
    for j in range(i, k+1):
        if i != j:
            if i%2 == 0 and j%2 == 1:
                cnt += 1
            elif i%2 == 1 and j%2 ==0:
                cnt += 1
print(cnt)