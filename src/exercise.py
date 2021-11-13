def main():
    # write your code below this line
    num = 1
    while num > 0:
        num = int(input('Give a number:\n'))
        if num < 0:
            print('Unsuitable number')
            num = int(input('Give a number:\n'))
        elif num == 0:
            num = num
        else:
            print(num*num)


if __name__ == '__main__':
    main()
