import os
from ClassTriagle import TriagleClass


intro ="""
--------------------------------------------------

    The program reads three integer values from
an input dialog. The three values represent the
lengths of the sides of a triangle. The program
displays a message that states whether the
triangle is scalene, isosceles, or equilateral.

--------------------------------------------------"""


os.system('cls')

print(intro)
inpout = 1


while inpout != 0 :

    newTriagle = TriagleClass()
    newTriagle.set_x()
    newTriagle.set_y()
    newTriagle.set_z()

    if newTriagle.isTriagle():
        newTriagle.typeOfTriagle()
        print("-"*50+
              "\n         Sides are sape a Triagle     \n") 
        print(  "         The triagle is {}".format(newTriagle.text))
  
    elif newTriagle.isZero():
        print( "-"*50+
              "\n                Error!! \n"+
                "    All sides mast greater than Zero!! \n"+ 
                "      All inputs mast be integers!! \n"+
                "       Sides are't sape a Triagle     ")
    else :
        print("-"*50+"\n"+
                "        Sides are't sape a Triagle     ")
        

  
    ##_____________________exit  while  menu         
    while True:
         query = input("\n"+("-"*50)+
                       " \nOK, now press Yes to continue or No to exit the programme: ")
         try:
             Fl = query[0].lower()
         except IndexError:
             Fl = 1
             break
         if query == '' or not Fl in ['y','n']:
            print('Please answer with yes or no!')
         else:
            break
    if Fl == 'y':
        inpout = 1
    if Fl == 'n':
        inpout = 0

    clear = lambda: os.system('cls')
    clear()
    print(intro)


