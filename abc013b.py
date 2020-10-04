a = int(input())
b = int(input())

cou1 = abs(a - b)
cou2 = abs(a-0)+abs(9-b) + 1
cou3 = abs(a-9)+abs(0-b) + 1

print(min(cou1,cou2,cou3))
