import math
from decimal import Decimal
a, b = map(float, input().split())
print(math.floor(Decimal(str(a))*Decimal(str(b))))