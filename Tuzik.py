## A wooden chest contains N coins. Tuzik is a little dog and he cannot
## open the chest by himself. Actually, the only thing he cando is use
## his barking to attract nearby people and seek their help. He can set
## the loudness of his barking precisely and therefore we can assume he can
## choose to call any number of people, from 1 to a maximum of K.
##
## When people come and open the chest they divide all the coins between them
## in such a way that everyone gets the same amount of coins and this amount is
## maximal possible. If some coins are not used they leave them on the ground and Tuzik
## will take them after they go away. Since, Tuzik is not a fool, he understands his profit
## depends upon the number of people he will call. While Tuzik works on his barking,
## you have to find the maximum possible number of coins he can get.


import math

if __name__ == "__main__":
    max_coin = -math.inf
    print("How many coins does the wooden chest have? ")
    N = int(input())
    print("Maximum people to be called ")
    K = int(input())

    for i in range(1, K+1, 1):
        remaining = N % i
        if remaining > max_coin:
            max_coin = remaining

    print(f"Max coins gained by Tuzik is {max_coin}")