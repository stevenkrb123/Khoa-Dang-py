def prime(x):
    if (x == 1):
        return False
    elif ( x == 2):
        return True
    else:
        for n in range(2,x):
            if(x % n == 0):
                return False
        return True
print(prime(3))