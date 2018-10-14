import numpy
_arrayDimension = input()
_arrayDimension = _arrayDimension.split()
_N = _arrayDimension[0]
_M = _arrayDimension[1]
_P = _arrayDimension[2]
_arrayOneInput = numpy.zeros((_N, _P), dtype=int)
_arrayTwoInput = numpy.zeros((_M, _P), dtype=int)
# N and _M are rows
# P is for column

counter = 0
while counter < _N:
    _arrayOneInput[counter] = input()
    counter = counter + 1
counter = 0
while counter < _M:
    _arrayTwoInput[counter] = input()
    counter = counter + 1
print(_arrayOneInput)

