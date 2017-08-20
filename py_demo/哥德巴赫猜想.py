# usr/bin/env python3
import time
from math import sqrt

start = time.time()
n = 100000
isprime = lambda p: all([p % d for d in range(2, int(sqrt(p)) + 1)])
# all(iterable): 如果iterable所有元素不为0、''、False或者iterable为空
# all(iterable)返回True 否则返回False
for i in range(6, n + 1, 2):
    for j in range(2, i // 2 + 1):
        if isprime(j) and isprime(i - j):
            break
    else:
        print('fail at {}'.format(i))
        break
    print('\r{:.2f}%'.format(i / n * 100), end='')

else:
    print('\nsuccess: all evens in {} is the sum of two primes.'.format(n))
end = time.time()
print('consum time: {:.3f} seconds'.format(end - start))