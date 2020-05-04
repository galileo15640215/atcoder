x = int(input())
c = 100
cnt = 0
while c < x:
    c += int(c*0.01)
    cnt += 1
print(cnt)