def split_and_join(line):
    _stringArray = line.split()
    return "-".join(_stringArray)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)