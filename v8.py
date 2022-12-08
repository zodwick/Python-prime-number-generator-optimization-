# added break
# filter out even
# filter out even in for loop directly
# limit search to half of i
# limit search to square root of i
# limit search to only previous prime numbers

# limit search to only previous prime numbers but checking for less than directly at list addition rather than during modulus
# check


import time
start = time.time()

c = 0
k = 1
l = []

for i in range(3, 100000, 2):

    for j in l:
        if i % j == 0:
            c += 1
            break
    if c == 0:
        k += 1
        if i < (100000**0.5):
            l.append(i)
    c = 0

print(k)

end = time.time()
print(end - start)


# time took
# 258.44545817375183
# 24.8780837059021
# 23.12345814704895
# 22.465441465377808
# 11.63539743423462
# 0.11180853843688965
# 0.09911322593688965
# 0.03931570053100586
