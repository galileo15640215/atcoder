t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    odd = 0
    even = 0
    for j in range(n):
        if a[j]%2 == 0:
            even += 1
        elif a[j]%2 == 1:
            odd += 1
    if even%2 == 0 and odd%2 == 0:
        print("YES")
    else:
        flag = True
        a.sort()
        j = 1
        flag = True
        while flag:
            flag = False
            while j < len(a):
                if a[j] - a[j-1] == 1:
                    a.pop(j-1)
                    a.pop(j-1)
                    even -= 1
                    odd -= 1
                    if even%2 == 0 and odd%2 == 0:
                        flag = False
                        break
                    flag = True
                elif a[j] - a[j-1] == 0:
                    if a%2 == 0:
                        even -= 2
                    else:
                        odd -= 2
                    a.pop(j-1)
                    a.pop(j-1)
                else:
                    j += 1
        odd = 0
        even = 0
        for j in range(len(a)):
            if a[j]%2 == 0:
                even += 1
            elif a[j]%2 == 1:
                odd += 1
        if even%2 == 0 and odd%2 == 0:
            print("YES")
        else:
            print("NO")