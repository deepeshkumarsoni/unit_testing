def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    if y is 0:
        raise ValueError('Cannot be divided by 0')
    return x/y
    
