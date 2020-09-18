## You are asked to ensure that the first and last names of people begin with a capital letter in their passports.
## For example, alison heck should be capitalised correctly as Alison Heck.
## alison heck => Alison Heck
## Given a full name, your task is to capitalize the name appropriately.


def capitalize(nameOrg):
    splitName = nameOrg.split(" ")
    capitalizedName = ""
    for i in range(len(splitName)):
        innerSplit = list(splitName[i])
        for j in range(len(innerSplit)):
            if j == 0:
                capitalizedName += innerSplit[j].upper()
            else:
                capitalizedName += innerSplit[j]
        capitalizedName += " "
    print(capitalizedName)


if __name__ == "__main__":
    name = input()
    capitalize(name)
