from math import sqrt as math_sqrt 
from math import cos as math_cos
from math import sin as math_sin 
from base_coordinate import BaseCartesian,BaseCircularCylindrial,BaceSpherialCoordinate


class Cartesian(BaseCartesian):
    # a point or a vector in cartesian
    
    def length_to_power_of_two(self):
        return (self.x*self.x) + (self.y*self.y) + (self.z*self.z)
    
    def length(self):
        return math_sqrt(self.length_to_power_of_two())

    
    def divide_by_num(self,num):
        if is_number(num):
            x=1.0*self.x/num
            y=1.0*self.y/num
            z=1.0*self.z/num
            return BaseCartesian(x,y,z)
    

    def product_by_num(self,num):
        if is_number(num):
            x=self.x*num
            y=self.y*num
            z=self.z*num
            return BaseCartesian(x,y,z)


    def get_unit_vector_3(self):
        return self.divide_by_num(length(vector))


    def __eq__(self,other_vector):
            if BaseCartesian.is_in_cartesian(other_vector):
                return (self.x==other_vector.x) and (self.y==other_vector.y) and (self.z==other_vector.z)
            return NotImplemented

    
    def __ne__(self,other_vector):
        if BaseCartesian.is_in_cartesian(other_vector):
            return (self.x!=other_vector.x) or (self.y!=other_vector.y) or (self.z!=other_vector.z)
        return NotImplemented

    
    def __add__(self,other_vector):
        if BaseCartesian.is_in_cartesian(other_vector):
            x=self.x+other_vector.x
            y=self.y+other_vector.y
            z=self.z+other_vector.z
            return BaseCartesian(x,y,z)
        
        return NotImplemented


    def __sub__(self,other_vector):
        if BaseCartesian.is_in_cartesian(other_vector):
            x=self.x-other_vector.x
            y=self.y-other_vector.y
            z=self.z-other_vector.z
            return BaseCartesian(x,y,z)
        
        return NotImplemented 


    def dot_product(self,other_vector):
        if BaseCartesian.is_in_cartesian(other_vector):
            return (self.x*other_vector.x)+(self.y*other_vector.y)+(self.z*other_vector.z)
        

    def cross_product(self,other_vector):
        if BaseCartesian.is_in_cartesian(other_vector):
            x=(self.y*other_vector.z) - (self.z*other_vector.y)
            y=(self.z*other_vector.x) - (self.x*other_vector.z)
            z=(self.x*other_vector.y) - (self.y*other_vector.x)
            return BaseCartesian(x,y,z)


    def projection(self,other_vector):
        ## projection of self along other_vector 
        if is_vector_3(other_vector):
            coefficient= 1.0*dot_product(self,ohter_vector)/(other_vector.length_to_power_of_two())
            return product_by_num(b,coefficient)
