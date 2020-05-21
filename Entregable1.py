import numpy as np
import matplotlib.pyplot as plt


m0=4*np.pi*10-7 #NPI
r0=[0,0]
m=[0,0.1]

x=np.linspace(-1,1,30) #Haciendo matriz
y=np.linspace(-1,1,30)
X,Y=np.meshgrid(x,y)

X_disp= X-r0[0] #Nuevas posiciones
Y_disp= Y-r0[1]

const=m0/(4*np.pi)#constante de la formula

mag=np.sqrt((X_disp**2)+(Y_disp**2))

Xunit=X_disp/mag
Yunit=Y_disp/mag

r =mag
rhat=[Xunit,Yunit]

producto= m[0]*rhat[0]+ m[1]*rhat[1]

bx=const*(3*rhat[0]*producto-m[0])/(r**3)
by=const*(3*rhat[1]*producto-m[1])/(r**3)

magB=np.sqrt((bx**2)+(by**2))

bxu= bx/magB
byu= by/magB

plt.figure(figsize=(16,8))

plt.subplot(1,2,1)
plt.quiver(X,Y,bxu,byu)
plt.title('Vectores Unitarios')

plt.subplot(1,2,2)
plt.streamplot(X,Y,bx,by)
plt.title('Lineas de trayectoria')

plt.figure(figsize=(10,10))

plt.quiver(X,Y,bxu,byu)
plt.streamplot(X,Y,bx,by)
plt.title('Combinación')

plt.show()