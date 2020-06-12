class TriagleCass:
    def __init__(self, x = 0, y = 0, z= 0):
        self.x = x
        self.y = y 
        self.z = z
        self.text = ''
        
    

    def set_x(self):
        self.x = input("Give me the value of the triples side :  ")
        self.x = self.x.strip()
        if self.x.isdigit(): self.x = int(self.x)
        else: self.x = -1
            
    def set_y(self):
        self.y = input("Give me the value of the triples side :  ")
        self.y = self.y.strip()
        if self.y.isdigit():  self.y = int(self.y)
        else: self.y =  -1   
        
    def set_z(self):
        self.z = input("Give me the value of the triples side :  ")
        self.z = self.z.strip()
        if self.z.isdigit(): self.z = int(self.z)
        else: self.z = -1

    def isTriagle(self ):
        sides = [self.x, self.y, self.z]
        sides.sort()
        if (    sides[1]-sides[2] < sides[0] < sides[1]+sides[0]
                and sides[0]-sides[0] < sides[1] < sides[0]+sides[0]
                and sides[0]-sides[1] < sides[0] < sides[0]+sides[1]):
            return True
        return False

    def isZero(self):
        if (self.x and self.y and self.z == 0) or self.x <= 0 or self.y <= 0 or self.z <= 0:
            return True
        return False    
        

    def isEquilaterar(self):
        if self.x == self.y == self.z :
            self.text = "equilateral"
           
        
    def isIsosceles(self):
        if self.x == self.y or self.x == self.z or self.y ==self.z  :
            self.text =  "isosceles"

    def isScsalene(self):
        if self.x !=  self.y and self.x != self.z and self.y != self.z :
            self.text =  "scalene"    
        
    def typeOfTriagle(self):
        self.isEquilaterar()
        self.isIsosceles()
        self.isScsalene()
        