n = int(input())
p = list(map(int, input().split()))
p0 = sorted(p)
key = 0
if p == p0:
    print("YES")
    key = 1
if key == 0:
    cnt = 0
    for i in range(len(p)):
        if p[i] != p0[i] and cnt == 0:
            idx1 = i
            cnt += 1
        elif p[i] != p0[i] and cnt == 1:
            idx2 = i
            cnt += 1
        if cnt >= 2:
            p[idx1], p[idx2] = p[idx2], p[idx1]
            if p == p0:
                print("YES")
                break
            else:
                print("NO")
                break
"""
    for i in range(len(p)):
        pt = p
        for j in range(len(p)):
            if i != j:
                pt[i], pt[j] = pt[j], pt[i]
                if pt == p0:
                    print("YES")
                    key = 1
                    break
"""                    
