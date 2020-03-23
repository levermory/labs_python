# sqrt decomposition

import math

#%%
array = list(range(1, 20))
print(array)

#%%
n = int(math.sqrt(len(array)))
print(n)

#%%
sums = []
sum = 0
for i in range(len(array)):
    sum += array[i]
    if (i+1) % n == 0:
        sums.append(sum)
        sum = 0
    elif i == len(array) - 1:
        sums.append(sum)
print(sums)

#%%
l = int(input('enter l: '))
print(l)

#%%
r = int(input('enter r: '))
print(r)

#%%
i = l
sum = 0
while i <= r:
    if i % n == 0 and i + n - 1 <= r:
        sum += sums[int(i / n)]
        i += n
    else:
        sum += array[i]
        i += 1

#%%
sum = 0
for i in range(2, 6):
    sum += array[i]
print(sum)
