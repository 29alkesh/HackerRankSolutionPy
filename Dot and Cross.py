import numpy
_arrayDimension = input()
_arrayDimension = _arrayDimension.split()
_N = int(_arrayDimension[0])

# N and _N are rows
# P is for column
_arrayOneInput = numpy.zeros((_N,1), dtype = list)
_arrayTwoInput = numpy.zeros((_N,1), dtype = list)
_arrayOneInputIntegers = numpy.zeros((_N,_N), dtype=int)
_arrayTwoInputIntegers = numpy.zeros((_N,_N), dtype=int)

counter = 0
while counter < _N:
    _arrayOneInput[counter] = input()
    counter = counter + 1
counter = 0
while counter < _N:
    _arrayTwoInput[counter] = input()
    counter = counter + 1
_arrayOneInput = _arrayOneInput.tolist()
_arrayTwoInput = _arrayTwoInput.tolist()
_arrayOneInputIntegers = _arrayOneInputIntegers.tolist()
_arrayTwoInputIntegers = _arrayTwoInputIntegers.tolist()

counter = 0
while counter < _N:
    _arrayOneInputIntegers[counter] = _arrayOneInput[counter][0].split()
    counter = counter + 1
counter = 0
while counter < _N:
    _arrayTwoInputIntegers[counter] = _arrayTwoInput[counter][0].split()
    counter = counter + 1
_arrayOneInputIntegers = numpy.array(_arrayOneInputIntegers)
_arrayOneInputIntegers = _arrayOneInputIntegers.astype(int)

_arrayTwoInputIntegers = numpy.array(_arrayTwoInputIntegers)
_arrayTwoInputIntegers = _arrayTwoInputIntegers.astype(int)


print(numpy.dot(_arrayOneInputIntegers,_arrayTwoInputIntegers))
