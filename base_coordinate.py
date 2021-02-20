
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


