import numpy
_arrayDimension = input()
_arrayDimension = _arrayDimension.split()
_N = int(_arrayDimension[0])
_M = int(_arrayDimension[1])

#_N = No. of Rows & _M = No. of Columns
if _N == _M :
    print(str(numpy.identity(_N)).replace('1',' 1').replace('0',' 0'))
else :
    print(str(numpy.eye(_N,_M, k = 0)).replace('1',' 1').replace('0',' 0'))
