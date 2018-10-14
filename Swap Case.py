def swap_case(s):
    _charactersArray = list(s)
    counter = 0
    while counter<len(_charactersArray):
        if _charactersArray[counter].islower():
            _charactersArray[counter] = _charactersArray[counter].upper()
        else:
            _charactersArray[counter] = _charactersArray[counter].lower()
        counter = counter + 1

    return ''.join(_charactersArray)


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)