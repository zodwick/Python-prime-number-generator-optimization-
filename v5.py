# added break
# filter out even
# filter out even in for loop directly
# limit search to half of i


import time
start = time.time()

c = 0
k = 1

for i in range(3, 100000, 2):

    for j in range(2, (i//2)):
        if i % j == 0:
            c += 1
            break
    if c == 0:
        k += 1
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
