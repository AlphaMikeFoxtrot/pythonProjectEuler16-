import string

def main():
    
    _file = open('names.txt', 'r')
    _list = []
    
    for i in _file.readlines():
        _list.append(i)
    
    newList = []
    
    for i in _list[0].split(','):
        newList.append(i)
    
    oldList = newList

    newList.sort()

    finalScore = 0

    for i in newList:
        finalScore += nameScore(i[1:len(i)-1], newList.index(i) + 1)

    print(finalScore)

def nameScore(name, pos):
    alphabets = list(string.ascii_uppercase)

    nameScore = 0

    for i in name:
        nameScore += alphabets.index(i) + 1

    return nameScore * pos
    

if __name__ == "__main__":
    main()
