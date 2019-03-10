import math
def true_multilateration(r1, r2, r3, U, Vx, Vy):
   V = math.sqrt(Vx**2 + Vy**2)
   x = (r1**2 - r2**2 + U**2)/(2*U)
   y = (r1**2 - r3**2 + V**2 - (2 * Vx * x))/(2*Vy)
   z = math.sqrt(r1**2 - x**2 - y**2)
   return (x, y, z)

r1 = float(input("Enter the value of r1:"))
r2 = float(input("Enter the value of r2:"))
r3 = float(input("Enter the value of r3:"))
U = float(input("Enter the value of U:"))
Vx = float(input("Enter the value of Vx:"))
Vy = float(input("Enter the value of Vy:"))

x,y,z = true_multilateration(r1,r2,r3,U,Vx,Vy)
print(round(x,3), round(y,3),round(z,3))