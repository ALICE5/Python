# Judge a number is a prime or not
import math
def isPrime(x):
    if x==1:
        return False
    k = int(math.sqrt(x))
    for j in range(2, k+1):
        if x % j == 0:
            return False
    return True

# Generate the num Prime
def prime(num):
    if num == 1:
        return 2
    k = 1
    i = 1
    while(k<num):
        i += 2
        if(isPrime(i)==True):
            k += 1
    return i

# Generate the no Monisen
def Monisen(no):
    k = 0
    i = 1
    m = 0
    while(k<no):
        p=prime(i)
        m = 2**p-1
        if(isPrime(m)==True):
            k+=1
        i+=1
    return m

if __name__ == '__main__':
    print(Monisen(6))
    # print(Monisen(int(input('Please input the number:'))))