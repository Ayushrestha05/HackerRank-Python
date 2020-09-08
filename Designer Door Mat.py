def design(N, M):
    for i in range(1, N, 2):
        print(((M - 3 * i) // 2) * '-' + i * '.|.' + ((M - 3 * i) // 2) * '-')
    print(((M - 7) // 2) * '-' + 'WELCOME' + ((M - 7) // 2) * '-')
    for i in range(N - 2, -1, -2):
        print(((M - 3 * i) // 2) * '-' + i * '.|.' + ((M - 3 * i) // 2) * '-')
    for i in range(1, n, 1):
        for j in range(1, m, 1):
            print('-')
    print('\n')


if __name__ == '__main__':
    userInput = input()
    split = userInput.split(' ')
    n = int(split[0])
    m = int(split[1])
    design(n, m)
