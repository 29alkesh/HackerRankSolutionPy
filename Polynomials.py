import numpy

_array1 = input()
_array1 = _array1.split()
_array1 = numpy.array(_array1)
_array1 = _array1.astype(float)
_x = int(input())
print(numpy.polyval(_array1, _x))

