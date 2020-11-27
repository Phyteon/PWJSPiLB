
import time
import random
import copy
from Res.task10_func import radix_lsd_sort
# LSD radix sorting algorithm
time_start = time.time()
randints = []
for i in range(0, 100000):
    randints.append(random.randint(0, 999))

good = copy.deepcopy(randints)
good.sort()
srtd = radix_lsd_sort(randints)
if good == srtd:
    print("Git")
