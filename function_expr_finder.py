from sympy import *


def calculate_polynomes(points):
    X = Symbol("x")
    polynomes = 0

    for xj, yj in points.items():
        other_cols = dict(set(points.items()) - {(xj, yj)})
        eq = 1
        
        for xi, yi in other_cols.items():
            eq *= expand((X-xi) / (xj-xi))
                
        polynomes = Add(polynomes, yj * eq)
        
    return simplify(polynomes)
    

points = {0: 0, -4: 0, 1: 1, 2: 1, 3: 0, 4: 2}

lagrange_polynomes = calculate_polynomes(points)

print(lagrange_polynomes)





