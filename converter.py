from math import pi as PI
from math import atan as math_atan

from base_coordinate import BaseCartesian,BaseCircularCylindrial,BaseSpherialCoordinate

class Converter:

    @staticmethod 
    def _calculate_teta_from_x_and_y(x,y):
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
    

    @staticmethod
    def check_cartesian(point):
        if not BaseCartesian.is_in_cartesian(point):
            raise ValueError('This point is not in Cartesian Coordinates')
        return True
    

    @staticmethod
    def check_circular_cylindrial(point):
        if not BaseCircularCylindrial.is_in_circular_cylindrail(point):
            raise ValueError('point is not in circular cylindrial')
        return True 
    

    @staticmethod
    def check_spherial_coordinate(point):
        if not BaceSpherialCoordinate.is_in_spherial_coordinate(point):
            raise ValueError('point is not in spherial coordinate')


    @staticmethod 
    def from_cartesian_to_circular_cylindrial(point):
        check_cartesian(point)
        # get data 
        x=point.x
        y=point.y
        z=point.z
        # calculate 
        r=math.sqrt( (x*x) + (y*y) )
        teta=_calculate_teta_from_x_and_y(x,y)
        return BaseCircularCylindrial(r,teta,z)
    

    @staticmethod
    def from_circular_cylindrial_to_cartesian(point):
        check_circular_cylindrail(point)
        # retrive data
        r=point.r
        teta=point.teta
        z=point.z
        # calculate 
        x=r*math_cos(teta)
        y=r*math_sin(teta)
        return BaseCartesian(x,y,z)


    @staticmethod
    def from_spherial_coordinate_to_cartesian(point):
        check_spherial_coordinate(point)
        # retrive data 
        r=point.r
        teta=point.teta
        phi=point.phi
        # calculate
        x=r*math_sin(phi)*math_cos(teta)
        y=r*math_sin(phi)*math_cos(teta)
        z=r*math_cos(phi)
        return BaesCartesian(x,y,z)


    @staticmethod 
    def from_cartesian_to_spherial_coordinate(point):
        check_cartesian(point)
        # retrive data
        x=point.x
        y=point.y
        z=point.z
        # calculate 
        r=math_sqrt( (x*x) + (y*y) + (z*z) )
        teta=_calculate_teta_from_x_and_y(x,y)
        phi=_calculate_phi_from_x_and_y_and_z(x,y,z)
        return BaseSpherialCoordinate(r,teta,phi)


    @staticmethod
    def from_spherial_coordinate_to_circular_cylindrial(point):
        check_spherial_coordinate(point)
        # retrive data 
        r=point.r
        teta=point.teta
        phi=point.phi
        # calculate
        in_cartesian=from_spherial_coordinate_to_cartesian(point)
        in_circular_cylindrial=from_cartesian_to_circular_cylindrial(in_cartesin)
        return in_circular_cylindrial


    @staticmethod 
    def from_circular_cylindrial_to_spherial_coordinate(point):
        check_circular_cylindrail(point)
        in_cartesian=from_circular_cylindrial_to_cartesian(point)
        in_spherial_coordinate=from_cartesian_to_spherial_coordinate(in_cartesian)
        return in_spherial_coordinate
