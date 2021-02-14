def mirror(alpha_list):
    if len(alpha_list) is 1:
        return alpha_list
    else:
        alpha_list_rev = alpha_list.copy()
        alpha_list_rev.reverse()
        return alpha_list[:-1]+alpha_list_rev

def print_rangoli(size):
    total_list = list()
    max_len = (size * 2 - 1) + (size * 2 - 2)
    for i in range(size):
        alpha_list = [chr(ord('a')+size-j-1)for j in range(i+1)]
        total_list.append("-".join(mirror(alpha_list)).center(max_len,"-"))
    print("\n".join(mirror(total_list)))
    # print(max_len)
    

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)