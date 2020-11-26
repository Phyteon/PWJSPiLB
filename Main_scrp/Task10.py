
import random
from Res.task10_func import radix_lsd_sort
# LSD radix sorting algorithm

randints = [101, 63, 50, 13, 10, 5, 3, 1]
# for i in range(0, 50):
#     randints.append(random.randint(0, 200))

srtd = radix_lsd_sort(randints)
