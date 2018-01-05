fact = 1

for i in range(1, 101):
    fact *= i

_list = []

for i in str(fact):
    _list.append(i)

sum = 0

for i in _list:
    sum += int(i)

print(sum)

print(_list)
