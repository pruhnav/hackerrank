import numpy
n,m = map(int,input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
mat = numpy.array(arr)
print(numpy.mean(mat, axis=1))
print(numpy.var(mat, axis=0))
print(round(numpy.std(mat, axis=None),11))
