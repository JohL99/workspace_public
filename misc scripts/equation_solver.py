from math import *
values = []


def get_values():
    x = int(input("How many values do you want to use?: "))
    global values
    for i in range(x):
        values.append(int(input("Choose an x value: ")))
    return True


def equ(eq, x, rnd):
    sol = eval(eq)
    print("y = " + str(round(sol, rnd)))
    return True

def main():
    if get_values():
        eq = input("What is the equation?: ")
        rnd = int(input("How many decimal places do you want?: "))
        for x in range(len(values)):
            equ(eq,values[x], rnd)
        print("complete")
        return 0
    print("failed")
    return 1

main()
