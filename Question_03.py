#Creating Sine,Cosine,Polynomial Curves
import matplotlib.pyplot as plt #importing neccesary packages
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
#creating functions for the particular curve
def sine_curve(): #The Sine Curve
 Fs= 8000
 f=5
 sample = 8000
 x=np.arange(sample)
 y=np.sin(2*np.pi*f*x/Fs)
 plt.plot(x, y)
 plt.xlabel('voltage(V)')
 plt.ylabel('sample(n)')
 plt.show()
def cosine_curve():#The Cosine Curve
 Fs = 8000
 f= 5
 sample= 8000
 x = np.arange(sample)
 y = np.cos(2*np.pi*f*x/Fs)
 plt.plot(x, y)
 plt.xlabel('voltage(V)')
 plt.ylabel('sample(n)')
 plt.show()
def polynomial_curve():#Polynomial Curve
 x= np.arange(-5, 5, 0.25)
 y= np.arange(-5, 5, 0.25)
 X, Y = np.meshgrid(x, y)
 F= 3+2*X + 4*X*Y + 5*X*X
 fig= plt.figure()
 ax= fig.add_subplot(111, projection='3d')
 ax.plot_surface(X, Y, F)
 plt.show()
def exponential_curve():#Exponential Curve
 time = np.arange(-2,2, 0.0001)
 constant = 0.8
 amplitude_grow = constant * np.exp(time)
 amplitude_decay = constant * np.exp(-time)
 plt.plot(time, amplitude_grow, time, amplitude_decay)
 plt.title('Exponential Curve', color='b')
 plt.xlabel('Time'+ r'$\rightarrow$')
 plt.ylabel('Amplitude '+ r'$\rightarrow$')
 plt.legend(['Growing Exponential','Decaying Exponential'])
 plt.grid()
 plt.axhline(y=0, color='k')
 plt.axvline(x=0, color='k')
 plt.show()
#creating menuBar & loop 
def menu():
 print('1. Sine Curve')
 print('2. Cosine Curve')
 print('3. Polynomial Curve')
 print('4. Exponential Curve')
ch = 'y'
while(ch=='y'):
  menu()
  choice = int(input('Enter choice(Like-1,2..etc):'))
  if(choice ==1):
   sine_curve()
  elif(choice==2):
   cosine_curve()
  elif(choice==3):
   polynomial_curve()
  elif(choice==4):
   exponential_curve()
  else:
   print('Wrong choice')
   ch = input('Do you want to continue (y/n)...')
