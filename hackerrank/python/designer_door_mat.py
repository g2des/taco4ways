if __name__ == "__main__":
    pattern = '.|.'
    welcome = 'WELCOME'
    height, width = tuple(map(int, input().rstrip().split()))
    for i in range(height):
        if i < height//2:
            print((pattern*(2*i+1)).center(width).replace(" ","-"))
        elif i == height//2:
            print(welcome.center(width).replace(" ","-"))
        else:
            print((pattern*(2*(height-i-1)+1)).center(width).replace(" ","-"))
        