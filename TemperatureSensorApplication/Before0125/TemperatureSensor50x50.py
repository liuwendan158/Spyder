

import serial
import numpy as np
from time import time
import matplotlib.pyplot as plt
import seaborn as sns
#from pylab import rcParams


M=np.zeros((50,50))
port = "COM5"
baud =   500000
temp = 0b101111
data = 0
header = 0
PressureArray=[]
X=[x for x in range(50)]
Y=[y for y in range(50)]
x,y=np.meshgrid(X, Y)
cmd="COM6"
#fig=plt.figure()
#plt.axes().set_aspect('equal')
row=0


def animate():
    df = np.zeros((50,50))
    while 1:
        for i in range(50):
            header=0
            data1=0
            row=0
            while(header != b'\xff'):
                header = ser.read(1)
            header=0
            data1=ser.read(2)
            if(data1==b'\xff\xff'):
                row=int.from_bytes(ser.read(1),'little')
                if row>50:
                    break;
                for j in range(50):
                    data=int.from_bytes(ser.read(2),byteorder='big')
                    #data2=((330 / (0.244141 * data/ 1000 + 2) * 10 - 100 - 800) / 8.7298)
                    if data==0:
                            data2=0
                    else:
                        data2=((3003 / ((0.292969 * data) / 1000 + 1.8)) - 834.66) / 8.7295
                    df[row,49-j] = data2
                row=0
                ser.read(1)
                data1=0
        yield df

            #plt.contourf(x,y,df, 50, cmap=plt.cm.jet,vmin=0, vmax=700)                             
            #plt.show()
           
ser = serial.Serial(port, baud, timeout=1)
if ser.isOpen():
     print(ser.name + ' is open...')

ss='run'+'\n'
ll=[ord(c) for c in ss]
ser.write(ll)


rw=animate()
M=next(rw)
past=time()

for i in range(6000):
    past=time()
    plt.clf()
    M=next(rw)
    CS=plt.contourf(X, Y, M, 50,origin='upper', cmap=plt.cm.jet)
    #sns.heatmap(M, vmax=50,cmap="plasma",cbar=True,square=True,annot=True)
	# use plt.contour to add contour lines
    #C = plt.contour(X, Y, M, 8, colors='black', linewidth=.5)
    #plt.clabel(C, inline=True, fontsize=10)
    
    #plt.imshow(M,origin='lower',vmin=0,vmax=50,cmap=plt.cm.jet)
    rightnow=time()
    gap=int(rightnow-past)
    plt.title('NAMI T Sensor')
    plt.xticks(())
    plt.yticks(())
    plt.figure("Nano and Advanced Materials Institue")
    plt.axes().set_aspect('equal')
    plt.colorbar(CS)
    #plt.figure(figsize=(10,10))
    #rcParams['figure.figsize'] = 10, 10
    plt.pause(0.03)



