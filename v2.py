# added break


import time
start = time.time()

c = 0
k = 0

for i in range(2, 100000):
    for j in range(2, i):
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
