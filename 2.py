t = int(input())
for i in range(t):
    n = int(input())
    s = list(map(int, input().split()))
    if n == 2:
        print(abs(s[0]-s[1]))
    else:
        s.sort()
        mi = 9999999999
        for j in range(1, n):
            if s[j] - s[j-1] < mi:
                mi = s[j] - s[j-1]
        print(mi)