data = [140, 4, 5, 6, 7, 8, 31, 32, 34, 45, 48,1, 2, 3, 125, 129, 130, 15]
print(len(data))
z=1
for j in range(len(data)-z):
    swapped = False
    for i in range(len(data)-z):
        if data[int(i)] > data[int(i+1)]:
            data[int(i)],data[int(i+1)] = data[int(i+1)],data[int(i)]
            swapped = True
    z = z + 1
    if not swapped:
    # ...то выходим из внешнего цикла.
        break
print(data)
