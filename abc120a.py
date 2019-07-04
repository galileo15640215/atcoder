a, b, c = map(int, input().split())
cnt = 0
for i in range(int(b/a)):
  cnt += 1
  if cnt == c:
    break
print(cnt)