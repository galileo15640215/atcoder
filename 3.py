n = int(input())
s = [list(input()) for i in range(n)]
for i in range(n-2, -1, -1):
    for j in range(1, 2*n-1):
        if s[i][j] == '#':
            if s[i+1][j-1] == 'X' or s[i+1][j] == 'X' or s[i+1][j+1] == 'X':
                s[i][j] = 'X'
for i in range(n):
    for j in range(2*n-1):
        print(s[i][j], end='')
    print()