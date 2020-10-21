maximun_number = 50
list=[]

def isPrimo(value):
    total = 0  # para saber se o as vez que e difisivel
    if value > maximun_number:
        print("valor assima do maximo")
    else:
        num = value
        for c in range(1,num + 1):  # em python tem que se somar mais um, o range quere dizer que cria uma lista do primeiro a ultimo numero
            if num % c == 0:
                total = total + 1
        if total == 2:
            n = 1
            list.append(c)
        else:
            n = 0
    return n


def main():
    print("Starting to computer prime number up to " + str(maximun_number))

    for i in range(0, maximun_number):
        if isPrimo(i):
            print('number' + str(i) + 'is prime')
            print(list)
        else:
            print('Number' + str(i) + 'is not prime')
            print(list)


if __name__ == "__main__":
    main()
