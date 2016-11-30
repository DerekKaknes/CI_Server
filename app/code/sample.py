import math
def add(x,y):
    return x + y

def is_prime(n):
    if type(n) != int:
        raise TypeError("n must be an integer")
    if n == 1:
        return False
    elif n < 1:
        raise ValueError("n cannot be less than 1")

    m = int(math.sqrt(n))
    for idx in range(2, m+1):
        if n % idx == 0:
            return False
    return True

def cubed(n):
    return 0
