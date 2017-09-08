# Write a Python class, Flower, that has three instance variables of type str, int, and float,
#  that respectively represent the name of the flower, its num- ber of petals, and its price.
#  Your class must include a constructor method that initializes each variable to an appropriate value,
#  and your class should include methods for setting the value of each type, and retrieving the value of
#   each type.


class Flower:

    def __init__(self,name,petals,price):
        self._name = name
        self._petals = petals
        self._price = price

    def setname(self,name):
        self._name = name

    def setpetals(self,petals):
        self._petals = petals

    def setprice(self,price):
        self._price = price

    def getname(self):
        return self._name

    def getpetals(self):
        return self._petals

    def getprice(self):
        return self._price



f1 = Flower('Dahlia',5,10.5)
print ("Name: ",f1.getname())
print ("Petals: ",f1.getpetals())
print ("Price: ",f1.getprice())

f1.setname('Rose')
f1.setpetals(10)
f1.setprice(5.5)
print ("Now F1 name: ",f1.getname())
print("Now F1 Petals: ",f1.getpetals())
print("Now f1 price: ",f1.getprice())
