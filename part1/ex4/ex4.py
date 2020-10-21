maximun_number=100

def isPerfect(value):
    num=value
    soma=0

    for c in range(1, num):
        if num % c==0:
            soma=soma+c
    if soma==num:
        return True
    else:
        return False
def main():
    print("Starting to compute perfect number up to " + str(maximun_number))

    for i in range(0, maximun_number):
        if isPerfect(i):
            print('number'+ str(i)+ 'is perfect')

if __name__=="__main__":
    main()