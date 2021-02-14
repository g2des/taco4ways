from itertools import groupby

a = list(map(str, input().strip()))

final = [str((len(list(g)), int(k))) for k, g in groupby(a)]
print(" ".join(final))
