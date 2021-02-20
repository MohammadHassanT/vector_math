import vector_3
from base_coordinate.BaseCoordinate import is_number 

class CircularCylindrial():
    def __init__(r,teta,z):
        if is_number(r,teta,z):
            self.r=r
            self.teta=teta
            self.z=z
