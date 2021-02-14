from itertools import combinations

options = list(map(str, input().strip().split()))
for i in range(1, int(options[1])+1):
    for pair in combinations(sorted(list(options[0])), i):
        print("".join(pair))

from itertools import combinations_with_replacement
for pair in combinations_with_replacement(sorted(list(options[0])), int(options[1])):
    print("".join(pair))

