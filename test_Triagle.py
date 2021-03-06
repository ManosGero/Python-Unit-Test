import unittest
import random
import string
from unittest import mock
from ClassTriagle import TriagleClass

class TestTriagle(unittest.TestCase):
    def test_init_(self):
    
        c = TriagleClass()
        self.assertEqual(c.x,0)
        self.assertEqual(c.y,0)
        self.assertEqual(c.z,0)
        
        for test_count in range(5000):
            x = random.randint(1,100001)
            y = random.randint(1,100001)
            z = random.randint(1,100001)
            c = TriagleClass(x, y, z)
            self.assertEqual(c.x,x)
            self.assertEqual(c.y,y)
            self.assertEqual(c.z,z)       
        
        for test_count in range(5000):
            x =randomString(random.randint(1,101))
            y = randomString(random.randint(1,101))
            z = randomString(random.randint(1,101))
            c = TriagleClass(x, y, z)
            self.assertEqual(c.x,0)
            self.assertEqual(c.y,0)
            self.assertEqual(c.z,0)  
        

    def test_isTriagle(self):
        c = TriagleClass(2 , 2 , 2)
        self.assertTrue(c.isTriagle() ) 
        c = TriagleClass(2 , 2 , 4)
        self.assertTrue(c.isTriagle() ) 
        c = TriagleClass(20 , 30 , 50)
        self.assertTrue(c.isTriagle() ) 
        c = TriagleClass(3 , 4 , 5)
        self.assertTrue(c.isTriagle() ) 
        
    def test_isNotTriagle(self):    
        c = TriagleClass(1 , 2 , 3)
        self.assertFalse(c.isTriagle() )         
        c = TriagleClass(0 , 0 , 0)
        self.assertFalse(c.isTriagle() )         
        c = TriagleClass(-1 , 4 , 5)
        self.assertFalse(c.isTriagle() )         
        c = TriagleClass("5" , 4 , 5)
        self.assertFalse(c.isTriagle() ) 
     
    def test_getX(self):
        for test_count in range(5000):
            c = TriagleClass()
            x =random.randint(1,101)
            with mock.patch('builtins.input', return_value = "{0} ".format(str(x))):
                c.set_x() 
                self.assertEqual(c.x,x) 
                                
    def test_getY(self):
        for test_count in range(5000):
            c = TriagleClass()
            y =random.randint(1,101)
            with mock.patch('builtins.input', return_value = "{0} ".format(str(y))):
                c.set_y() 
                self.assertEqual(c.y,y) 

    def test_getZ(self):
        for test_count in range(5000):
            c = TriagleClass()
            z =random.randint(1,101)
            with mock.patch('builtins.input', return_value = "{0} ".format(str(z))):
                c.set_z() 
                self.assertEqual(c.z,z)              
           
    def test_isZero(self):
        for test_count in range(5000):
            x =random.randint(0,1)
            y =random.randint(0,1)
            z =random.randint(0,1)
            if x ==1 and y == 1 and z ==1: x=0
            c = TriagleClass()
            self.assertTrue(c.isZero())
            
    def test_isEquilaterar(self):      
        for test_count in range(5000):
            x = random.randint(1,100001)
            c = TriagleClass(x , x , x) 
            c.isEquilaterar()
            self.assertEqual(c.text,"equilateral")
            
    def test_isIsosceles(self):      
        for test_count in range(5000):
            x = random.randint(1,100001)
            y = random.randint(1,100001)
            if x==y: y+=1
            c = TriagleClass(x , y , y) 
            c.isIsosceles()
            self.assertEqual(c.text,"isosceles")
            c = TriagleClass(y , x , y)  
            c.isIsosceles()
            self.assertEqual(c.text,"isosceles")
            c = TriagleClass(y , y , x)  
            c.isIsosceles()
            self.assertEqual(c.text,"isosceles")
            
            
    def test_isScsalene(self):      
        for test_count in range(5000):
            x = random.randint(1,100001)
            y = random.randint(1,100001)
            if x==y: y+=1
            z = random.randint(1,100001)
            if x==z: z+=1
            if y==z: z+=1
            
            c = TriagleClass(x , y , z)  
            c.isScsalene()
            self.assertEqual(c.text,"scalene")
            
            c = TriagleClass(x , z, y)  
            c.isScsalene()
            self.assertEqual(c.text,"scalene")
            
            c = TriagleClass(z , x , y)  
            c.isScsalene()
            self.assertEqual(c.text,"scalene")
            
            c = TriagleClass(z , y , x)  
            c.isScsalene()
            self.assertEqual(c.text,"scalene")
            
            c = TriagleClass(y , z , x)  
            c.isScsalene()
            self.assertEqual(c.text,"scalene")
            
            c = TriagleClass(y , x , z)  
            c.isScsalene()
            self.assertEqual(c.text,"scalene")           

    #def test_typeOfTriagle(self):
            
            
def randomString(stringLength=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))
    
    
if __name__ == "__main__":
    unittest.main()