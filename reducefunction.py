from functools import reduce
num=[1,2,3,4]
a=reduce(lambda x,y:x+y,num)                                  K
print(a)
import functools  #2ND METHOD
num=[1,2,3,4]
a=functools.reduce(lambda x,y:x+y,num)                               
print(a)
