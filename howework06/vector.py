from __future__ import annotations
from math import sqrt

class Vector:
    def __init__(self, *args):
        self.points = list(args)

    def __str__(self):
        if len(self.points) > 0:        
            return 'Vector = '+(', '.join(str(x) for x in self.points))
        return 'Vector = empty'
    
    def __bool__(self):
        return not(self.points[0] == 0 and len(set(self.points))==1)
    
    def __add__(self, other_vector: Vector):
        result = []
        for x,y in [self.points, other_vector.points]:
            result.append(x+y)
        return Vector(tuple(result))
    
    def __sub__(self, other_vector: Vector):
        result = []
        for x,y in [self.points, other_vector.points]:
            result.append(x-y)
        return Vector(tuple(result))
    
    def __mul__(self, other_vector: Vector):
        result = []
        for x,y in [self.points, other_vector.points]:
            result.append(x*y)
        return Vector(tuple(result))

    def __eqq__(self, other_vector: Vector):
        for x,y in [self.points, other_vector.points]:
            if(x!=y):return False
        return True
    
    def __len__(self):
        return(len(self.points))
    
    def __abs__(self):
        return round( sqrt(sum([x*x for x in self.points])) ,2)
    
    def __scalar_multiplication__(self, number:float):
        for index in range(len(self.points)):
            self.points[index] *= number
            
    def __scalar_division__(self, number:float):
        for index in range(len(self.points)):
            self.points[index] /= number

    def __negation__(self):
        for index in range(len(self.points)):
            self.points[index] *= -1

    
vector1 = Vector(3,4)
print(vector1)
print(vector1.__bool__())
vector2 = Vector(2,3)
print(vector1.__add__(vector2))
print(vector1.__sub__(vector2))
print(vector1.__eqq__(vector2))
print(vector1.__len__())
print(vector1.__abs__())
