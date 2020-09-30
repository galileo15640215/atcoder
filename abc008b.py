N = int(input())
dic = {}
for _ in range(N):
  S = input()
  if S not in dic:
    dic[S] = 1
  else:
    dic[S] += 1
    
ans = sorted(dic.items(), key=lambda x: x[1], reverse=True)[0][0]
print(ans)
