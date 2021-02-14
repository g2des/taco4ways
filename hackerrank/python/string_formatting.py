def print_formatted(number):
    max_len = len(str(bin(number))[2:])
    for i in range(number):
        deci = i + 1
        octi = str(oct(deci))[2:].upper()
        hexi = str(hex(deci))[2:].upper()
        bini = str(bin(deci))[2:].upper()
        print(str(deci).rjust(max_len),
                octi.rjust(max_len),
                hexi.rjust(max_len),
                bini.rjust(max_len))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)