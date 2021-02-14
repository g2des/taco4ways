from itertools import combinations
if __name__ == "__main__":
    n = int(input().strip())
    alphas = list(map(str, input().split()))
    k = int(input().strip())
    temp = [int('a' in combo) for combo in combinations(alphas, k) ]
    print(sum(temp)/len(temp))