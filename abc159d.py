n = int(input())
a = list(map(int, input().split()))
nums = [0 for i in range(n)]
sum = 0
for i in range(n):
    nums[a[i]-1] += 1
for i in range(n):
    t = nums[i]
    sum += t*(t-1)//2
for i in range(n):
    t = nums[a[i]-1]
    print(sum - t*(t-1)//2 + (t-1)*(t-2)//2)