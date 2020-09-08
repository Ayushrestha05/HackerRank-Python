def split_and_join(line):
    # write your code here
    spliiter = line.split(" ")
    split1 = "-".join(spliiter)
    return split1

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)