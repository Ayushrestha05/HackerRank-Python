## When we perform leftRotations=2. the array undergoes the following sequence of changes:
## [1,2,3,4,5] -> [2,3,4,5,1] -> [3,4,5,1,2]


print("Enter left rotations")
leftRotations = int(input())
a = [1, 2, 3, 4, 5]
for i in range(0, leftRotations, 1):
    firstElement = a.pop(0)
    a.append(firstElement)
print(a)
