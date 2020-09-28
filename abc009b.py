n = int(input())
A = sorted(set([int(input()) for _ in range(n)]), reverse=True)
print(A[1])