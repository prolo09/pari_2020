#!/usr/bin/env python

import readchar

listCharAsc = []


def printALLCharsUpTO():
    print ("intreduza um carater :")
    stop_char = readchar.readchar()

    charInAscii = ord(stop_char)  # ord serve para por em ascii

    for x in range(32, charInAscii):
        xChar = chr(x)  # passa de ascii para o seu carater
        listCharAsc.append(xChar)


# _______________ ex 4.b_____________________

def readAllUPTO():
    print ("intreduza carater:")
    intVariavel = readchar.readchar()

    while intVariavel != 120:
        intVariavel = readchar.readchar()
        intVariavel = ord(intVariavel)
        if intVariavel == 120:
            break
        else:
            print ("volte a inserir:")


# ______________ex 4.c_______________________


def countNumberUPTO():
    total_number = 0
    total_other = 0


    while True:
        print ("intreduza carater:")
        intVariavel = readchar.readchar()

        '''????????????????????????????????????nao endendo mesmo poque o isnumber nao esta a dar so funciona no python 3 posso usar  is digital'''

        if intVariavel.isdigit()==True:
            total_number = total_number + 1

        else:
            total_other = total_other + 1


        intVariavel = ord(intVariavel)

        if intVariavel != 120:
            print ("intreduza o valor outra vez :")

        else:
            break

    print ("you entered " + str(total_number) + "numbers.")
    print ("you entered " + str(total_other) + "others.")


def main():
    printALLCharsUpTO()
    print (listCharAsc)
    readAllUPTO()
    countNumberUPTO()


if __name__ == '__main__':
    main()
