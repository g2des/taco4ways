
def jumpingOnClouds(c):
    steps = 0
    current_index = 0
    print(c)
    while current_index +1 != len(c):
        if current_index +2 < len(c) and c[current_index+2] !=1:
            current_index +=2
        else:
            current_index+=1
        print(current_index)
        steps+=1
    return steps

if __name__ == "__main__":
    n = int(input().strip())
    c = list(map(int, input().rstrip().split()))
    result = jumpingOnClouds(c)
    print(result)