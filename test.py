import math

def round_down(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n * multiplier) / multiplier


print(round_down(0.299999999999999999999999999999999999999999999999999999999999999999999999 , 2))


