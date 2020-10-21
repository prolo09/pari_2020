maximun_number=100


from my_fuc import  isPerfect
# ou import mu_fuc
# depois possos por my_fuc as mf (e assim posso escrever na frente do codigo so escrevendo mf )

def main():
    print("Starting to compute perfect number up to " + str(maximun_number))

    for i in range(0, maximun_number):
        if isPerfect(i):
            print('number'+ str(i)+ 'is perfect')

if __name__=="__main__":
    main()