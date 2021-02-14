def count_substring(string, sub_string):
    len_sub = len(sub_string)
    len_str = len(string)
    return sum([sub_string == string[i:i+len_sub] for i in range(len_str-len_sub+1)])

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)