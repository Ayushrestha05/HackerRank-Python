if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    # loops as long as the input number is given
    for _ in range(n):
        # Splits the input into name variable and line variable
        name, *line = input().split()
        # Converts the input in line variable into scores list
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    sum1 = 0.0
    for i in range(len(student_marks[query_name])):
        sum1 = sum1 + student_marks[query_name][i]
    avg = sum1 / len(student_marks[query_name])
    print("%.2f" % avg)
