import numpy

_arrayDimension = input()
_arrayDimension = _arrayDimension.split()
_arrayDimension = list(map(int, _arrayDimension))
_arrayInput = numpy.empty((_arrayDimension[0], 1), dtype=list)
_arrayInputIntegers = numpy.zeros((_arrayDimension[0], _arrayDimension[1]), dtype=int)
i = 0
j=0
while i < _arrayDimension[0]:
    _arrayInput[i] = input()
    i = i + 1
i = 0
_arrayInput = _arrayInput.tolist()

_arrayInputIntegers = _arrayInputIntegers.tolist()


while i < _arrayDimension[0]:
    _arrayInputIntegers[i] =_arrayInput[i][0].split()
    i = i+1

_arrayInputIntegers = numpy.array(_arrayInputIntegers)
_arrayInputIntegers = _arrayInputIntegers.astype(int)
numpy.set_printoptions(legacy='1.13')
print(numpy.mean(_arrayInputIntegers,axis=1),numpy.var(_arrayInputIntegers,axis=0),round(numpy.std(_arrayInputIntegers,axis=None),12),sep="\n")