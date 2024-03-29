import math

def optic_ratio(temp_tuple):
    global r1
    global r2
    global r3
    r1 = (.035*3.3)/(temp_tuple[0]*2*.0014)
    r2 = (.035*3.3)/(temp_tuple[1]*2*.0014)
    r3 = (.035*3.3)/(temp_tuple[2]*2*.0014)
    print(r1, r2, r3)
#Vy is distance from yellow ball to pink ball
#Vx is x component of distance from yellow to pink
#U distance between pink and blue
def true_multilateration(U, Vx, Vy):
   V = math.sqrt(Vx**2 + Vy**2)
   x = (r1**2 - r2**2 + U**2)/(2*U)
   y = (r1**2 - r3**2 + V**2 - (2 * Vx * x))/(2*Vy)
   print(x, y)
   z = math.sqrt(r1**2 - x**2 - y**2)
   return (x, y, z)