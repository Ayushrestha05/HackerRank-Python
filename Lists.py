if __name__ == '__main__':
    command_list = []
    output_list = []
    N = int(input())
    for _ in range(N):
        command = input()
        command_list.append(command)

    for i in range(len(command_list)):
        current_command = command_list[i]
        command_name, *v1 = current_command.split()
        variables = list(map(int, v1))

        if command_name == 'insert':
            output_list.insert(variables[0], variables[1])
        elif command_name == 'print':
            print(output_list)
        elif command_name == 'remove':
            output_list.remove(variables[0])
        elif command_name == 'append':
            output_list.append(variables[0])
        elif command_name == 'sort':
            output_list.sort()
        elif command_name == 'pop':
            output_list.pop()
        elif command_name == 'reverse':
            output_list.reverse()
        else:
            print("Wrong Error entered in line", i)
