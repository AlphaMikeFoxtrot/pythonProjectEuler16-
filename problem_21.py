sum = 0
_dict = {}

for i in range(1, 10000):
    for j in range(1, i + 1):
        if(i % j == 0):
            sum += j

    _dict[i] = sum - i
    sum = 0

for i in _dict:
    print("key : {}\tvalue : {}".format(i, _dict[i]))

final = 0

for i in _dict:
    key = i + 1
    valueOne = _dict[i]
    if valueOne in _dict:
        valueTwo = _dict[valueOne]
        if(i == _dict[_dict[i]] and i != _dict[i]):
            final += _dict[_dict[i]]
            print("d({}) = {}\td({}) = {}".format(i, _dict[i], _dict[i], _dict[_dict[i]]))

print(final)
