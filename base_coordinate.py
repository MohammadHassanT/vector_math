from math import pi as PI

###############################################
class BaseCoordinate:
    
    @staticmethod
    def _is_number(a):
        return (isinstance(a,(int,float))) and (not isinstance(a,bool))

    @staticmethod
    def is_number(*args):
        for num in args:
            if not BaseCoordinate._is_number(num):
                raise ValueError(f'This {num} is not a number')
        if not args:
            raise ValueError('None is not a number')
        return True
###############################################

class BaseCartesian:
    # a point or a vector in cartesian

    def __init__(self,x,y,z):
        if BaseCoordinate.is_number(x,y,z):
            self.x=x
            self.y=y
            self.z=z

    @staticmethod
    def _is_in_cartesian(a,BaseCartesian):
        return isinstance(a,BaseCartesian)

    @staticmethod
    def is_in_cartesian(*args):
        for vector in args:
            if not _is_in_cartesian(vector):
                raise ValueError('This is not an instance of Cartesian class')
        if not args:
            raise ValueError('didn\'t expected None')
        return True

    def __str__(self):
        return f'x={self.x}\ty={self.y}\tz={self.z}'
##############################################

class BaseCircularCylindrial:

    @staticmethod
    def is_in_r_bound(r):
        if r >= 0:
            return True
        raise ValueError(f'In circular cylindrail coordiante r must be greater than or equal zero. {r} is not')

    @staticmethod
    def is_in_teta_bound(teta):
        if (teta >= 0) and (teta < (2*PI)):
            return True        
        raise ValueError(f'In circular cylindrail coordiante teta must be >= 0 and <= 2*pi. {teta} is not')

    def __init__(self,r,teta,z):
        # teta is in radian 
        if BaseCoordinate.is_number(r,teta,z):
            if self.is_in_r_bound(r) and self.is_in_teta_bound(teta):
                self.r=r
                self.teta=teta
                self.z=z
    
    @staticmethod 
    def _is_in_circular_cylindrial(test):
        return isinstance(test,BaseCircularCylindrial)
    
    @staticmethod
    def is_in_circular_cylindraid(*args):
        for test in args:
            if not _is_in_circular_cylindrial(test):
                raise ValueError('This is not an instance of Circular Cylindrail class')
        if not args:
            raise ValueError('didn\'t expected None')
        return True

    def __str__(self):
        return f'r={self.r}\tteta={self.teta}\tz={self.z}'

########################################################

class BaseSpherialCoordinate:
    
    @staticmethod
    def is_in_r_bound(r):
        if r >= 0:
            return True
        raise ValueError(f'In spherial coordinates r must be greater than equal zero. {r} is not.')
    
    @staticmethod
    def is_in_teta_bound(teta):
        if (teta >= 0) and (teta < (2*PI)):
            return True
        raise ValueError(f'In spherial coordinates teta must be between 0 and 2*pi(not 2*pi itself). {teta} is not')
    
    @staticmethod
    def is_in_phi_bound(phi):
        if (phi >= 0) and (phi < PI):
            return True
        raise ValueError(f'In spherial coordinates phi must be between 0 and pi(not pi itself). {phi} is not')

    def __init__(self,r,teta,phi):
        if BaseCoordinate.is_number(r,teta,phi):
            if is_in_r_bound(r) and is_in_teta_bound(teta) and is_is_phi_bound(phi):
                self.r=r
                self.teta=teta
                self.phi=phi

    @staticmethod
    def _is_in_spherial_coordinate(test):
        return isinstance(test,BaseSpherialCoordinates)

    @staticmethod
    def is_in_spherial_coordinate(*args):
        for test in args:
            if not _is_in_circular_cylindrial(test):
                raise ValueError('This is not an instance of Spherial Coordinates class')
        if not args:
            raise ValueError('didn\'t expected None')
        return True

    def __str__(self):
        return f'r={self.r}\tteta={self.teta}\tphi={self.phi}'

#########################################
