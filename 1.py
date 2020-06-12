n = int(input())
a = [list(map(int, input().split())) for i in range(n-1)]
dic = {}
for i in range(n-1):
    dic[a[i][0]] = []
    dic[a[i][1]] = []
for i in range(n-1):
    dic[a[i][0]].append([a[i][1], a[i][2])
    dic[a[i][1]].append([a[i][0], a[i][2])
st = []
st.append(dic[1])
while st:
    st.pop(-1)