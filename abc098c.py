n = int(input())
s = input()
c = [0 for i in range(n)]
for i in range(0+1, n):
    if s[i] == 'E':
        c[0] += 1

for i in range(1, n):
    c[i] = c[i-1]
    if s[i] == 'E':
        c[i] -= 1
    if s[i-1] == 'W':
        c[i] += 1
print(min(c))