from time import time, ctime
import math
data=ctime()

print ("a data e" + data)

time1=time()

for i in range(0, 50000000):
    math.sqrt(i)

time2=time()

timetotal=time2-time1

print ('o tempo total e :' + str(timetotal) )





