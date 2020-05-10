n = int(input())
v = list(map(int, input().split()))
odd = {}
even = {}
for i in range(n):
    if i%2 == 1:
        if v[i] not in odd:
            odd[v[i]] = 1
        else:
            odd[v[i]] += 1
    else:
        if v[i] not in even:
            even[v[i]] = 1
        else:
            even[v[i]] += 1
if len(odd) == 1 and len(even) == 1:
    if odd.keys() == even.keys():
        print(n//2)
    else:
        print(0)
else:
    mx1 = 0
    mx2 = 0
    for i in odd.keys():
        if mx1 < odd[i]:
            mx2 = mx1
            mx1 = odd[i]
            nx = i
        elif mx2 < odd[i]:
            mx2 = odd[i]
    my1 = 0
    my2 = 0
    for i in even.keys():
        if my1 < even[i]:
            my2 = my1
            my1 = even[i]
            ny = i
        elif my2 < even[i]:
            my2 = even[i]
    if nx == ny:
        if mx1 > my1:
            print(n - mx1 - my2)
        else:
            print(n - mx2 - my1)
    else:
        print(n - mx1 - my1)