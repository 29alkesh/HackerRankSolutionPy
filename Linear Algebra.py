import numpy
_n = int(input())

_arrayOneInput = numpy.zeros((_n,1), dtype = list)
_arrayOneInputIntegers = numpy.zeros((_n,_n), dtype=float)
counter = 0
while counter < _n:
    _arrayOneInput[counter] = input()
    counter = counter + 1
counter = 0

while counter < _n:
    _arrayOneInputIntegers[counter] = _arrayOneInput[counter][0].split()
    counter = counter + 1
counter = 0

_arrayOneInputIntegers = numpy.array(_arrayOneInputIntegers)
_arrayOneInputIntegers = _arrayOneInputIntegers.astype(float)

print(round(numpy.linalg.det(_arrayOneInputIntegers),2))