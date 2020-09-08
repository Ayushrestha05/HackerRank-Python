def mutate_string(string, position, character):
    mutate = list(string)
    mutate[position] = character
    output = ""
    for i in range (len(mutate)):
        output = output + mutate[i]
    return output

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)