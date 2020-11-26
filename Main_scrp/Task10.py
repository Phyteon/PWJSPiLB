
import random
from Res.task10_func import radix_lsd_sort
# LSD radix sorting algorithm

randints = []
for i in range(0, 20):
    randints.append(random.randint(0, 999))

print(randints)
srtd = radix_lsd_sort(randints)
print(srtd)