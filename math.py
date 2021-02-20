from math import sqrt


dimention=3


def _is_number(a):
    return (isinstance(a,(int,float,complex))) and (not isinstance(a,bool))


def is_number(a):
    if not _is_number(a):
        raise ValueError('this is not a number')
    return True


def _is_vector_3(a):
    global dimention
    return (type(a) is list) and (len(a) == dimention)


def is_vector_3(a):
    if not _is_vector_3(a):
        raise ValueError('This is not a vector')
    return True


def _length_3(a):
    return sqrt( (a[0]*a[0]) + (a[1]*a[1]) + (a[2]*a[2]) )


def length_3(a):
    if is_vector_3(a):
        return _length_3(a)


def _vector_3_divide_by_num(vector,num):
    global dimention
    output=[]
    for c in range(0,dimention):
        output.append(1.0*vector[c]/num)
    return output


def vector_3_divide_by_num(vector,num):
    if is_number(num) and is_vector_3(vector):
        return _vector_3_divide_by_num(vector,num)


def _vector_3_product_by_num(vector,num):
    global dimention
    output=[]
    for c in range(0,dimention):
        output.append(vector[c]*num)
    return output


def vector_3_product_by_num(vector,num):
    if is_vector_3(vector) and is_number(num):
        return _vector_3_product_by_num(vector,num)


def get_unit_vector_3(vector):
    return vector_3_divide_by_num(vector,length_3(vector))


def _plus_3(a,b):
    global dimention
    output=[]
    for c in range(0,dimention):
        output.append(a[c]+b[c])
    return output


def _minus_3(a,b):
    global dimention
    minus_b=[]
    for c in range(0,dimention):
        minus_b.append((-1)*b[c])
    return _plus_3(a,minus_b)


def plus_3(a,b):
    if is_vector_3(a) and is_vector_3(b):
        return _plus_3(a,b)


def minus_3(a,b):
    if is_vector_3(a) and is_vector_3(b):
        return _minus_3(a,b)


def _dot_product(a,b):
    return a[0]*b[0] + a[1]*b[1] + a[2]*b[2]


def dot_product(a,b):
    if is_vector_3(a) and is_vector_3(b):
        return _dot_product(a,b)


def _cross_product(a,b):
    output=[]
    output.append(a[1]*b[2]-a[2]*b[1])
    output.append(a[2]*b[0]-a[0]*b[2])
    output.append(a[0]*b[1]-a[1]*b[0])
    return output


def cross_product(a,b):
    if is_vector_3(a) and is_vector_3(b):
        return _cross_product(a,b)


def _projection(a,b):
    ## projection of a along b
    coefficient= 1.0*_dot_product(a,b)/(b[0]*b[0]+b[1]*b[1]+b[2]*b[2])
    return _vector_3_product_by_num(b,coefficient)


def projection(a,b):
    if is_vector_3(a) and is_vector_3(b):
        return _projection(a,b)

