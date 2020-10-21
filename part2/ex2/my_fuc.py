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