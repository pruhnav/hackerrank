import numpy

n, m = map(int, input().split())

arr = []

for i in range(n):
    arr.append(list(map(int, input().split())))

print(numpy.max(numpy.min(arr, axis=1)))
