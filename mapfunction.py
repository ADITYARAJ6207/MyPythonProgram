a=[1,2,3,4]  #map function using lambda function
b=list(map(lambda x:x*x,a))
print(b)
a=[1,2,3,4]    #map function without lambda function

def square(x):
    return x*x
b=list(map(square,a))
print(b)
