n, m, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ni = 0
mi = 0
now = 0
cnt= 0
while True:
    if ni < n and mi < m:
        if a[ni] <= b[mi] and now + a[ni] <= k:
            now += a[ni]
            ni += 1
            cnt += 1
        elif a[ni] >= b[mi] and now + b[mi] <= k:
            now += b[mi]
            mi += 1
            cnt += 1
        else:
            break
    elif ni < n:
        if now + a[ni] <= k:
            now += a[ni]
            ni += 1
            cnt += 1
        else:
            break
    elif mi < m:
        if now + b[mi] <= k:
            now += b[mi]
            mi += 1
            cnt += 1
        else:
            break
    else:
        break
print(cnt)