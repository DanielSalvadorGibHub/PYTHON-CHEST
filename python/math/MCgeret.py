import random as rd

for xxx in range(3):
    result = False
    while result == False:
        var1 = rd.randint(0,1)
        var2 = rd.randint(0,1)
        print(f"{var1}  {var2}"*12)
        result = True
