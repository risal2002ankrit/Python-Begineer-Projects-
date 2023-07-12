import matplotlib.pyplot as plt

x1= [2, 4, 5, 6]
y1= [2, 3, 6, 7]

plt.plot(x1, y1, label = 'line 1')

x2=[1, 2, 3, 4]
y2= [1, 2, 4, 4]
plt.plot(x2, y2, label = 'line 2')

plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Demo Graph- two lines')
plt.legend()
plt.show()
