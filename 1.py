n = int(input())
a = list(map(int, input().split()))
l = [0 for i in range(51)]
for i in range(n):
    l[a[i]] += 1
flag = False
for i in range(len(l)):
    if l[i] >= 4:
        flag = True
if flag:
    print("YES")
else:
    print("NO")