import numpy
_array = input()
_array = _array.split()
_array = numpy.array(_array)
_array = _array.astype(float)
numpy.set_printoptions(sign=' ')
print(numpy.floor(_array))
print(numpy.ceil(_array))
print(numpy.rint(_array))