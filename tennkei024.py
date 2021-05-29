n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
flag = True
sua = sum(a)
sub = sum(b)
if abs(sua%2 - sub%2) != k%2:
    flag = False
elif abs(sua - sub) > k:
    flag = False
if flag:
    print("Yes")
else:
    print("No")
