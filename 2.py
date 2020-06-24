t = int(input())
for i in range(t):
    s = input()
    for j in range(len(s)):
        if s[j] == '1' and s[i+1] == '0'