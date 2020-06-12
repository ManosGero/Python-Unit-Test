import os 
def isInt(var):
    if var==int(var):
        return True
    return False

intro ="""
--------------------------------------------------

    The program reads three integer values from
an input dialog. The three values represent the
lengths of the sides of a triangle. The program
displays a message that states whether the
triangle is scalene, isosceles, or equilateral.

--------------------------------------------------"""

def getInt():
        x = input("Give me the value of the triples side :  ")
        x = x.strip()
        if x.isdigit(): return int(x)
        return -1

def triagle(x,y,z):
    sides = [x,y,z]
    sides.sort()
    if (    sides[1]-sides[2] < sides[0] < sides[1]+sides[0]
            and sides[0]-sides[0] < sides[1] < sides[0]+sides[0]
            and sides[0]-sides[1] < sides[0] < sides[0]+sides[1]):
        return True
    return False
        
####################################################################
#                         Main programm                            #
####################################################################

os.system('cls')
print(intro)
inpout = 1
anser = '' 
while inpout != 0 :
    
    a = getInt()
    b = getInt()
    c = getInt()

    if a<0 or b <0 or c< 0 or a == 0 or b == 0 or c == 0:
        print("-"*50+
              "\n             Error!! \n"+
                " All sides mast greater than Zero!! \n"+
                " All inputs mast be integers!! \n")
        anser = "False valiue"
     
    elif triagle(a,b,c):
        print("-"*50+
              "\n         Sides are sape a Triagle     \n")
        
        if a == b == c:
            anser = "equilateral"
            print("         The tragle is {}".format(anser))
        elif a == b or a == c or b ==c :
            anser = "isosceles"
            print("         The tragle is {}".format(anser))
        elif a !=  b and a != c and b != c:
            anser = "scalene"
            print("         The tragle is {}".format(anser))
    else:
        print("-"*50+
              "\n         Sides are't sape a Triagle     \n")
        anser = "Not triagle"
            






    ##############         exit  while  menu          ############# 
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

    os.system('cls')
    print(intro)


