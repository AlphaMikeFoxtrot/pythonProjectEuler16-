import itertools

string = ""

for i in sorted(list(itertools.permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])), key=lambda x: x[1])[1000000]:
    string += str(i)

print (string)
