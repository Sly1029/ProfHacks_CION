import math
global r1
global r2
global r3

def optic_ratio(temp_tuple, ratio):
    r1 = temp_tuple[0]*ratio
    r2 = temp_tuple[1]*ratio
    r3 = temp_tuple[2]*ratio

def true_multilateration(U, Vx, Vy):
   V = math.sqrt(Vx**2 + Vy**2)
   x = (r1**2 - r2**2 + U**2)/(2*U)
   y = (r1**2 - r3**2 + V**2 - (2 * Vx * x))/(2*Vy)
   z = math.sqrt(r1**2 - x**2 - y**2)
   return (x, y, z)