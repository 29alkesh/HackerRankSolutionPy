import numpy

_array1 = input()
_array1= _array1.split()
_array2 = input()
_array2= _array2.split()
_array1 = numpy.array(_array1)
_array2 = numpy.array(_array2)
_array1 = _array1.astype(int)
_array2 = _array2.astype(int)
print(numpy.inner(_array1, _array2))
print(numpy.outer(_array1, _array2))