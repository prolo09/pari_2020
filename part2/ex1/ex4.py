#! /home/pedrorolo/Documents/5ANO/PARI/part2/ex1
# ____________________
# A simple python scritp to print hello wold
# Pedro Rolo
# Pari, Outobro 2020
# _____________________


maximun_number = 100


def isPerfect(value):
    """
esta funcao reporna os prefeitos
    :param value:  tem um valor de entrada
    :return: o o valor perfeito
    """
    num = value
    soma = 0

    for c in range(1, num):
        if num % c == 0:
            soma = soma + c
    if soma == num:

        return True
    else:
        return False


def main():
    print("Starting to compute perfect number up to " + str(maximun_number))

    for i in range(0, maximun_number):
        if isPerfect(i):
            print('number' + str(i) + 'is perfect')


if __name__ == "__main__":
    main()
