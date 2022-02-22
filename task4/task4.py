with open(input(), 'r', encoding='utf-8') as array_file:
    array = sorted(list(map(int, array_file.readlines())))
median = array[len(array)//2]
steps = 0
for i in array:
    steps += abs(median - i)
print(steps)
