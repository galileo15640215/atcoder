import sys
from math import ceil
input = sys.stdin.readline
a, b = map(int, input().split())
print(ceil((a+b)/2))