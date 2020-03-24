# sqrt decomposition

# %%
import random

file = open('requests.txt', 'w')
n = 10
for i in range(n):
    l = random.randint(0, 18)
    r = random.randint(l, 18)
    file.write(str(l) + ' ' + str(r) + '\n')
file.close()

# %%
import math

array = range(1, 20)
n = int(math.sqrt(len(array)))
sums = []
sum = 0
for i in range(len(array)):
    sum += array[i]
    if (i + 1) % n == 0:
        sums.append(sum)
        sum = 0
    elif i == len(array) - 1:
        sums.append(sum)


def request(some_var="0 18"):
    """Returns subsum of the array(sum
     of elements from l to r). Request must
     be a string of 2 integers and a space
     between them, e.g.: "4 5"."""

    some_var = some_var.split()
    l = int(some_var[0])
    r = int(some_var[1])
    sum = 0
    if l == r:
        return array[l]
    while l <= r:
        if l % n == 0 and l + n - 1 <= r:
            sum += sums[int(l / n)]
            l += n
        else:
            sum += array[l]
            l += 1
    return sum


file = open('requests.txt', 'r')
for line in file:
    print(request(line))
