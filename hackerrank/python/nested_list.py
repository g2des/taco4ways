from operator import itemgetter
if __name__ == '__main__':
    scores = list()
    second_lowest = None
    for _ in range(int(input())):
        name = input()
        score = float(input())
        scores.append([name, score])
    scores.sort(key=itemgetter(1,0))
    minVal = min(scores, key=itemgetter(1))[1]
    # print(scores, minVal)
    for score in scores:
        if score[1] != minVal and second_lowest is None:
            second_lowest = score[1]
            # print(second_lowest)
        if score[1] == second_lowest:
            print(score[0])
        

    