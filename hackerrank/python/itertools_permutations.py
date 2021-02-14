from itertools import permutations
options = list(map(str, input().strip().split()))
for pair in sorted(permutations(options[0], int(options[1]))):
    print("".join(pair))