n = int(input())
ans = [0 for i in range(n+1)]
for x in range(1, 100):
    for y in range(1, 100):
        for z in range(1, 100):
            tmp = x**2 + y**2 + z**2 + x*y + y*z + z*x
            #print(x, y, z, tmp)
            if 1 <= tmp and tmp <= n:
                ans[tmp] += 1
for i in range(1, n+1):
    print(ans[i])
"""
for i in range(n+1):
    tmp = i+1
    cnt = 0
    for x in range(1, min(tmp//3, 20)):
        for y in range(1, min(tmp//3, 20)):
            if 4*tmp - 3*x**2 - 2*x*y - 3*y**2 >= 0:
                z = 0.5*(-(4*tmp - 3*x**2 - 2*x*y - 3*y**2)**0.5 - x - y)
                if 1 <= z and z%1 == 0:
                #if x**2 + y**2 + z**2 + x*y + y*z + z*x == tmp:
                    cnt += 1
                z = 0.5*((4*tmp - 3*x**2 - 2*x*y - 3*y**2)**0.5 - x - y)
                if 1 <= z and z%1 == 0:
                #if x**2 + y**2 + z**2 + x*y + y*z + z*x == tmp:
                    cnt += 1
print(cnt)
"""
