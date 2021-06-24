# -*- coding: utf-8 -*-
"""serial_chase_problem.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1f832uGyWQ_04YNFiHLJCNdT7ktoGHkF8
"""

import math
def dis(x1,y1,x2,y2):
  return math.sqrt((x1-x2)**2 + (y1-y2)**2)

x_A=[10]
y_A=[0]
x_B=[0]
y_B=[10]
x_C=[10]
y_C=[10]
x_D=[0]
y_D=[0]

v_A=3
v_B=5
v_C=7
v_D=2

D_got_shoot = 0
B_got_shoot = 0
C_got_shoot = 0


distDA= dis(x_D[0],y_D[0],x_A[0],y_A[0])
distCB= dis(x_C[0],y_C[0],x_B[0],y_B[0])
distBD= dis(x_B[0],y_B[0],x_D[0],y_D[0])

for t in range(1,21):
  #D is chased by A target-D 
  sin = (y_D[t-1]- y_A[t-1]) / distDA
  cos= (x_D[t-1] - x_A[t-1]) / distDA
  new_x_A= x_A[t-1]+ v_A* cos
  new_y_A= y_A[t-1] + v_A*sin
  x_A.append(new_x_A)
  y_A.append(new_y_A)

  #C is chased by B Target- C 
  sin = (y_C[t-1]- y_B[t-1]) / distCB
  cos= (x_C[t-1] - x_B[t-1]) / distCB
  new_x_B= x_B[t-1]+ v_B* cos
  new_y_B= y_B[t-1] + v_B*sin
  x_B.append(new_x_B)
  y_B.append(new_y_B)

  #B is chased by D
  sin = (y_B[t-1] - y_D[t-1]) / distBD
  cos = (x_B[t-1] - x_D[t-1]) / distBD
  new_x_D =  x_D[t-1] + v_D * cos
  new_y_D =  y_D[t-1] + v_D * sin
  x_D.append(new_x_D)
  y_D.append(new_y_D)

  x_C.append(x_C[t-1])
  y_C.append(y_C[t-1] + v_C)

  distDA= dis(x_D[t],y_D[t],x_A[t],y_A[t])
  distCB= dis(x_C[t],y_C[t],x_B[t],y_B[t])
  distBD= dis(x_B[t],y_B[t],x_D[t],y_D[t])


  if distDA<5:
    print("t = ",t)
    print("distance_of_DA = " , distDA)
    print("A shoot D")
    D_got_shoot = D_got_shoot + 1

  if distCB<5:
    print("t = ",t)
    print("distance_of_CB = " , distCB)
    print("B shoot C")
    C_got_shoot = C_got_shoot + 1

  if distBD<5:
    print("t = ",t)
    print("distance_of_BD = " , distBD)
    print("D shoot B")
    B_got_shoot = B_got_shoot + 1


print("B_got_shoot = ",B_got_shoot)
print("C_got_shoot = ",C_got_shoot)
print("D_got_shoot = ",D_got_shoot)

import matplotlib.pyplot as plt
plt.plot( x_A,y_A, color='yellow', linewidth=2, label ='A')
plt.plot( x_B,y_B, color='black', linewidth=2, label ='B')
plt.plot( x_C,y_C, color='blue', linewidth=2, label ='C')
plt.plot( x_D,y_D, color='green', linewidth=2, label ='D')
plt.legend()