s = input()
n = int(s[0])*100 + int(s[1])*10 + int(s[2])
for i in range(1, len(s)-2):
    if abs(753-n) > abs(753-(int(s[i])*100 + int(s[i+1])*10 + int(s[i+2]))):
        n = int(s[i])*100 + int(s[i+1])*10 + int(s[i+2])
print(abs(753-n))