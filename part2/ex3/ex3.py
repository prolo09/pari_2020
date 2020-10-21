maximun_number=50
import  argparse


def isPrimo(value):
    total=0 #para saber se o as vez que e difisivel
    if value>maximun_number:
        print("valor assima do maximo")
    else:
        num=value
        for c in range(1, num+1): # podia ir em vez de ao valor ate a raiz quadrada int round(math.sqrt(value))
          if num % c==0:
              total=total+1
        if total==2:
            n=1
        else:
            n=0
    return n


# podia por assim
# for i in range(2, value)
# if not value % i:
# return False


def main():

ap=argparse.ArgumentParser(description='process some integres.')
ap.add_argument('max_number' , type=int)


    print("Starting to computer prime number up to " + str(maximun_number))

    for i in range(0, maximun_number):
        if isPrimo(i):
            print('number'+str(i)+'is prime')
        else:
            print('Number' + str(i)+'is not prime')

if __name__=="__main__":
   main()


