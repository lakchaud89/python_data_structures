class Vector:

    def __init__(self,d):
        self._coords = [0] * d

    @classmethod
    def vector(self,seq):
        self._coords = [0] * len(seq)
        for i in range(len(seq)):
            self._coords[i] = seq[i]

    def __len__(self):
        return len(self._coords)

    def __getitem__(self,j):
        return self._coords[j]

    def __setitem__(self,j,val):
        self._coords[j] = val

    def __add__(self,other):
        if(len(self)!=len(other)):
            raise ValueError("dimensions must agree")
        else:
            result = Vector(len(self))
            for i in range(len(self)):
                result[i] = self[i]+other[i]
        return result

    def __radd__(self,other):
        if(len(self)!=len(other)):
            raise ValueError("dimensions must agree")
        else:
            result = Vector(len(self))
            for i in range(len(self)):
                result[i] = self[i]+other[i]
        return result

    def __eq__(self,other):
        return self._coords == other._coords

    def __ne__(self,other):
        return not self == other

    def __str__(self):
        return "<"+str(self._coords)+">"

    def __sub__(self,other):
        if (len(self)!=len(other)):
            raise ValueError("dimensions must agree")
        else:
            result = Vector(len(self))
            for i in range(len(self)):
                result[i] = self[i] - other[i]
        return result

    def __neg__(self):
        for j in range(len(self)):
            self[j] = -self[j]
        return self

    # def __mul__(self,n):
    #     for i in range(len(self)):
    #         self[i] *= n
    #     return self

    def __rmul__(self,n):
        for i in range(len(self)):
            self[i] *= n
        return self

    def __mul__(self,other):
        if (len(self)!=len(other)):
            raise ValueError("dimensions must agree")
        else:
            result = 0
            for i in range(len(self)):
                result += self[i]*other[i]
            return result

u = Vector(3)
v = Vector(3)

print("Vector u : ",str(u))
print("Vector v : ", str(v))
u[0] = 1
u[1] = 2
u[2] = 3
v[0] = 4
v[1]= 5
v[2]= 6
print("Vector u : ",str(u))
print("Vector v : ", str(v))
uv_add = u+v
print("uv_add: ", str(uv_add))
uv_sub = u - v
print("uv_sub: ", str(uv_sub))
u_neg = -u
v_neg = -v
print("u_neg :", str(u_neg))
print("v_neg : ", str(v_neg))

# u_mul = u * 3
# print("u_mul: ",str(u_mul))
# u_rmul = 3 * u
# print("u_rmul: ", str(u_rmul))
uv_mul = u * v
print("uv_mul : ", str(uv_mul))

z = u + [5, 3, 10]
print("z : ", str(z))

y = [5, 3, 10]  + u
print("y : ", str(y))

vec_obj = Vector.vector([5,6,7,8])
print("vec_obj: ", str(vec_obj))
