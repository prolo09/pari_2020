from collections import namedtuple

Complex = namedtuple('complex',['r','i'])

def addComplex(x,y):




def  multiplyComplex(x,y):




def printComplex(x):




def main():

    c1=Complex(5,3)
    c2=Complex
    print('c1= ' + str(c1))

    c3=addComplex(c1,c2)
    printComplex(c3)

    printComplex(multiplyComplex(c1,c2))


if __name__ == '__main__':
    main()