n = int(input())
s = [input() for i in range(n)]
c = [0 for i in range(4)]
for i in range(n):
    if s[i] == "AC":
        c[0] += 1
    elif s[i] == "WA":
        c[1] += 1
    elif s[i] == "TLE":
        c[2] += 1
    elif s[i] == "RE":
        c[3] += 1
print("AC x "+str(c[0]))
print("WA x "+str(c[1]))
print("TLE x "+str(c[2]))
print("RE x "+str(c[3]))