import numpy
_input = input()
_input = list(map(int, _input.split()))
print(numpy.zeros(_input, dtype = numpy.int))
print(numpy.ones(_input, dtype = numpy.int))