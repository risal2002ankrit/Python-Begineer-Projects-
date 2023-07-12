import matplotlib.pyplot as plt

x= [2, 4, 5, 6]
y= [2, 3, 6, 7]

plt.plot(x, y, color='green',linestyle='dashed', linewidth=3, marker='o', markerfacecolor='blue', markersize=12)
plt.ylim(1, 8)
plt.xlim(1, 8)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('customized graph')
plt.show()
