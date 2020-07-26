n, k = map(int, input().split())
a = list(map(int, input().split()))
rui = []
su = 1
for i in range(k):
    su *= a[i]
rui.append(su)
for i in range(k, n):
    rui.append(rui[-1]*a[i]//a[i-k])
for i in range(1, len(rui)):
    if rui[i] > rui[i-1]:
        print("Yes")
    else:
        print("No")
