def l_insert(obj, options):
    num = int(options[1])
    pos = int(options[2])
    obj.insert(num, pos)

def l_print(obj, options):
    print(obj)

def l_remove(obj, options):
    num = int(options[1])
    obj.remove(num)

def l_append(obj, options):
    num = int(options[1])
    obj.append(num)

def l_sort(obj, options):
    obj.sort()

def l_pop(obj, options):
    obj.pop()

def l_reverse(obj, options):
    obj.reverse()

def actions(obj_list):
    options = str(input()).split(" ")
    funcList = {
        "insert": l_insert,
        "append": l_append,
        "remove": l_remove,
        "reverse": l_reverse,
        "pop": l_pop,
        "sort":l_sort,
        "print":l_print,
    }
    funcList[options[0]](obj_list, options)


if __name__ == '__main__':
    obj_list = list()
    N = int(input())
    for _ in range(N):
        actions(obj_list)
    