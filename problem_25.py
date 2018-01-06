fib = 1
first = 1
second = 1
third = 1

_list = [1, 1]

while len(str(fib)) != 1000:
    third = first + second
    first = second
    second = third
    fib = third
    _list.append(fib)
    third = 0

print(len(_list))
