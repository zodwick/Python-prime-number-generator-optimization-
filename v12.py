# added break
# filter out even
# filter out even in for loop directly
# limit search to half of i
# limit search to square root of i
# limit search to only previous prime numbers

# limit search to only previous prime numbers but checking for less than directly at list addition rather than during modulus
# check

# taking finding of sqrt of final number as constant outside
# implementing sieve method?
# final optimised version of sieve check . multiples of 2 removed during set creation

import time
start = time.time()
n = 100000
numbers = set(range(3, n+1 , 2))
primes = []

while numbers:
    p = numbers.pop()
    primes.append(p)
    numbers.difference_update(set(range(2*p, n+1, p)))
    # 2*p as p(the first element of numbers) was already removed as part of pop() function


print(len(primes)+1)

end = time.time()
print(end - start)


# time took (seconds)
# 258.44545817375183
# 24.8780837059021
# 23.12345814704895
# 22.465441465377808
# 11.63539743423462
# 0.11180853843688965
# 0.09911322593688965
# 0.03931570053100586
# 0.03710675239562988
# 0.020193815231323242
# 0.015111684799194336
