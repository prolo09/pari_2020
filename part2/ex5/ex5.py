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

    inputs = [] # crio a list de imputs

    while True:
        print ("intreduza carater:")
        intVariavel = readchar.readchar()

        inputs.append(intVariavel)  # acrecenta varaiveis no input

        # retiri o isnumeric pois so dava para python3 e nao tinha conseguido fazer isso anteriormente

        intVariavel = ord(intVariavel)

        if intVariavel != 120:
            print ("intreduza o valor outra vez :")

        else:
            break

    # para destingir se e numero ou nao

    for input in inputs:  # vai correndo as variaveis que tenho nas listas



        if input.isdigit():
            total_other = total_number + 1
        else:
            total_number = total_number + 1

    print ("you entered " + str(total_number) + "numbers.")
    print ("you entered " + str(total_other) + "others.")


    # ex 5c

    dict_other={}

    for idx,input in enumerate(inputs): # o enumerate inumera as variavais para outra variavel que tinhamos
        if not input.isdigit():
            dict_other[idx]=input # add new key-value to dictianary


    print ('dint_other '+ str(dict_other))


    # ex 5c

    # use de sort na lista e organiza sozinho as variaveis ...



def main():
    printALLCharsUpTO()
    print (listCharAsc)
    readAllUPTO()
    countNumberUPTO()


if __name__ == '__main__':
    main()
