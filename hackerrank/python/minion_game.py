def minion_game(string):
    stuart = 0
    kevin = 0
    for i in range(len(string)):
        count = len(string) - i
        if string[i].lower().startswith(('a','e','i','o','u')):
            kevin+=count
        else:
            stuart+=count
    if stuart > kevin:
        print("Stuart {}".format(stuart))
    elif kevin > stuart:
        print("Kevin {}".format(kevin))
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)