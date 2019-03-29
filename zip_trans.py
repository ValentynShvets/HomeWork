array = [
    [1, 2, 3, 'a'],
    [4, 5, 6, 'b'],
    [7, 8, 9, 'c'],
    [10, 11, 12, 'd']
]

array = zip(*array)
for i in array:
    print(*i)
