def swap_case(s):
    newstring = ''
    for a in s:
        if a.isupper():
            newstring += (a.lower())
        elif a.islower():
            newstring += (a.upper())
        elif a.isspace():
            newstring += a
        else:
            newstring += a
    return newstring


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
