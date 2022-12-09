import math

def alpha(n):
    def inner_alpha(r):
        area = ((n*(r**2))/2)*math.sin(math.radians(360/n))
        return area
    return inner_alpha


def polygon_area(n,r):
    if n<= 0 or isinstance(n, str) or isinstance(r,str):
        return 'input must be a positive number'
    else:
        res = alpha(n)(r)
        if math.sin(res) < 0 and math.cos(res) <0: return 'quadrant 3, imaginary'
        elif math.sin(res) < 0 and math.cos(res)> 0: return 'quadrant 4, imaginary'
        else: return res
        

print(polygon_area(1.3,7))
print(polygon_area(9,21))
print(polygon_area(360,21))
print(polygon_area(-5,21))
