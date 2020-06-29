d = int(input())
c = list(map(int, input().split()))
s = [list(map(int, input().split())) for i in range(d)]
mem = [0 for i in range(26)]
v = 0
su = sum(c)
for a in range(d):
    print(d%26+1)