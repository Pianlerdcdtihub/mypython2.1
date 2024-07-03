


def F(c):
        x = 9/5*c+32
        print("องศาฟาเรนไฮส์ = %d"% x)
        return x
    
def K(c):
        y = c+273.15
        print("องศาเควิน = %d " % y)
        return y

c = int(input("องศา: "))
K(c)
F(c)