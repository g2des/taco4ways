
def repeatedString(s, n):
    num_fullstring = n // len(s)
    len_partString = n%len(s)
    num_a_full = 0
    num_a_part = 0
    for char in s:
        if char == 'a':
            num_a_full+=1
    for char in s[:len_partString]:
        if char == 'a':
            num_a_part += 1
    return num_a_full * num_fullstring + num_a_part


if __name__ == "__main__":
    s = input()
    n = int(input().strip())
    result = repeatedString(s, n)
    print(result)