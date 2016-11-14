def distance(x1, y1, x2, y2):
    import math
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx**2 + dy**2
    ans = math.sqrt(dsquared)
    return ans
