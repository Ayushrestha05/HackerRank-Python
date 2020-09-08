# Given the participants' score sheet for your University Sports Day,
# you are required to find the runner-up score. You are given N scores.
# Store them in a list and find the score of the runner-up.
# The first line contains N. The second line contains an array A[] of integers each separated by a space.
# Print the runner-up score. i.e. second maximum number

if __name__ == '__main__':
    def array_maker(arr):
        for x in arr:
            a1.append(x)


    n = int(input())
    arr = map(int, input().split())
    a1 = []
    array_maker(arr)
    output = 0
    max_val = max(a1)
    arr_val = -100
    for i in range(len(a1)):
        if arr_val < a1[i] < max_val:
            arr_val = a1[i]
            output = a1[i]
    print(output)
