## You are given a positive integer N.
## Your task is to print a palindromic triangle of size N

if __name__ == "__main__":
    for i in range(1, int(input()) + 1):
        print(int(10 ** i / 9) * int(10 ** i / 9))