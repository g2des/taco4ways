from itertools import product

a = list(map(int, input().strip().split()))
b = list(map(int, input().strip().split()))

axb = [str(x) for x in product(a, b)]

print(" ".join(axb))