from base_coordinate import BaseCartesian,BaseCircularCylindrial,BaseSpherialCoordinates
from math import pi as PI
from math import atan as math_atan

class CircularCylindrial(BaseCircularCylindrial):
    
    def _calculate_teta_form_x_and_y(x,y):
        if x==0 and y==0:
            # there is no equivalent form teta so we set it to zero
            teta=0
        elif x==0 and y>0:
            teta=PI/2.0
        elif x==0 and y<0:
            teta=1.5*PI
        elif y==0 and x>0:
            teta=0
        elif y==0 and x<0:
            teta=PI
        # until now we have considered every point in x and y axes 
        elif x>0 and y>0:
            teta=math_atan(1.0*y/x)
        elif x>0 and y<0:
            teta=2*PI+math_atan(1.0*y/x)
        elif x<0: # y either is greater that 0 or smaller that 0,
            teta=PI+math_atan(1.0*y/x)
        return teta

    @classmethod
    def from_cartesian(cls,point_in_cartesian):
        if not BaseCartesian.is_in_cartesian(point_in_cartesian):
            raise ValueError('This point is not in Cartesian Coordinates')
        # get data 
        x=point_in_cartesian.x
        y=point_in_cartesian.y
        z=point_in_cartesian.z
        # calculate 
        r=math.sqrt( (x*x) + (y*y) )
        teta=_calculate_teta_from_x_and_y(x,y)
        return cls(r,teta,z)

    
