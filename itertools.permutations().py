from itertools import permutations
_input = input()
_input = _input.split()
print(*[''.join(i) for i in permutations(sorted(_input[0]),int(_input[1]))],sep='\n')