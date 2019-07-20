n, d = map(int, input().split())
if d == 1 and n%((d*2)+1) == 0:
    print(int(n/(d*2+1)))
elif d == 1:
    print(int(n/(d*2+1))+1)
elif d*2+1 >= n:
    print(1)
elif n%((d*2)+1) == 0:
    print(int(n/(d*2+1)))
else:
    print(int(n/(d*2+1))+1)