#!/usr/bin/env python
def addComplex(x,y):
    P0= x[0]+y[0]
    P1=x[1]+y[1]
    P=(P0,P1)
    return P

def multiplyComplex(x,y):

    P0= x[0]*y[0]-x[1]*y[1]
    P1=x[0]*y[1]+x[1]*y[0]
    P=(P0,P1)
    return P

def printComplex(x):
    print (str(x[0]) + "+" +str(x[1])+ "i")


def main():
    # ex2 a)

    c1=(5,3)
    c2=(-2,7)
    # test add
    c3=addComplex(c1,c2)
    printComplex(c3)

    # test multplic
    printComplex(multiplyComplex(c1,c2))



if __name__ == '__main__':
    main()