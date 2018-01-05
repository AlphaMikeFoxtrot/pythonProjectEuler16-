# maximum path sum I

def main():

    _file = open('triangle.txt', 'r')
    triangle = []

    for i in _file.readlines():
        triangle.append(list(i.rstrip().split(' ')))

    while(len(triangle) != 1):
        for number in triangle[-2]:
            triangle[-2][triangle[-2].index(number)] = int(triangle[-2][triangle[-2].index(number)]) + int(max(triangle[-1][triangle[-2].index(
                number)], triangle[-1][triangle[-2].index(number) + 1]))
        triangle.remove(triangle[-1])

    print(triangle)

if __name__ == "__main__":
    main()
