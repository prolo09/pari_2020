#!/usr/bin/env python
from collections import namedtuple

Complex = namedtuple('complex',['r','i'])

def addComplex(x,y):
    z_r=x['r']+y['r']
    z_i=x['i']+y['i']

    return Complex(r=z_r,i=z_i)



def  multiplyComplex(x,y):
    z_r = x[0] * y[0] - x[1] * y[1]
    z_i = x[0] * y[1] + x[1] * y[0]

    return Complex(r=z_r, i=z_i)


def printComplex(x):
    print (str(x[0]) + "+" + str(x[1]) + "i")




def main():

    c1=Complex(5,3)
    c2=Complex
    print('c1= ' + str(c1))

    c3=addComplex(c1,c2)
    printComplex(c3)

    printComplex(multiplyComplex(c1,c2))


if __name__ == '__main__':
    main()