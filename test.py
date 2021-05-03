import math
import define

def round_down(n, decimals=0):
    multiplier = 10 ** decimals
    return int(math.floor(n * multiplier)) / multiplier


print(round_down(0.29999999999 , 10))


