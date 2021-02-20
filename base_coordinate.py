# I have nothing to import 

class BaseCoordinate:
    
    @staticmethod
    def _is_number(a):
        return (isinstance(a,(int,float))) and (not isinstance(a,bool))

    @staticmethod
    def is_number(*args):
        for num in args:
            if not _in_number(num):
                raise ValueError(f'This {num} is not a number')
        return True


class BaseCartesian(BaseCoordinate):
    # a point or a vector in cartesian

    def __init__(self,x,y,z):
        if is_number(x,y,z):
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
        return True


class BaseCircularCylindrial(BaseCoordinate):

    @staticmethod
    def is_in_r_bound(r):
        if r >= 0:
            return True
        raise ValueError(f'In circular cylindrail coordiante r must be greater than or equal zero. {r} is not')

    @staticmethod
    def is_in_teta_bound(teta):
        if (teta >= 0) and (teta < (2*math.pi)):
            return True        
        raise ValueError(f'In circular cylindrail coordiante teta must be >= 0 and <= 2*pi. {teta} is not')

    def __init__(self,r,teta,z):
        # teta is in radian 
        if is_number(r,teta,z):
            if is_in_r_bound(r) and is_in_teta_bound(teta):
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
        return True


class BaseSpherialCoordinates(BaseCoordinate):
    
    @staticmethod
    def is_in_r_bound(r):
        if r >= 0:
            return True
        raise ValueError(f'In spherial coordinates r must be greater than equal zero. {r} is not.')
    
    @staticmethod
    def is_in_teta_bound(teta):
        if (teta >= 0) and (teta < (2*math.pi)):
            return True
        raise ValueError(f'In spherial coordinates teta must be between 0 and 2*pi(not 2*pi itself). {teta} is not')
    
    @staticmethod
    def is_in_phi_bound(phi):
        if (phi >= 0) and (phi < math.pi):
            return True
        raise ValueError(f'In spherial coordinates phi must be between 0 and pi(not pi itself). {phi} is not')

    def __init__(self,r,teta,phi):
        if is_number(r,teta,phi):
            if is_in_r_bound(r) and is_in_teta_bound(teta) and is_is_phi_bound(phi):
                self.r=r
                self.teta=teta
                self.phi=phi

    @staticmethod
    def _is_in_spherial_coordinates(test):
        return isinstance(test,BaseSpherialCoordinates)

    @staticmethod
    def is_in_spherial_coordinates(*args):
        for test in args:
            if not _is_in_circular_cylindrial(test):
                raise ValueError('This is not an instance of Spherial Coordinates class')
        return True

