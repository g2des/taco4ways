
def counting_valleys(steps, path):
    path = list(path)
    count_valleys = 0
    current_altitude = 0
    for val in path:
        num = -1 if val == "D" else 1
        if current_altitude < 0 and current_altitude + num == 0:
            count_valleys +=1
        current_altitude += num
    return count_valleys

if __name__ == "__main__":
    steps  = int(input().strip())
    path = input()
    result = counting_valleys(steps, path)
    print(result)