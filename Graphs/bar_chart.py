import matplotlib.pyplot as plt

left= [1,2,3,4,5]
height= [10,11,23,36,4]

tick_label= ['one', 'two', 'three', 'four', 'five']
plt.bar(left, height, tick_label= tick_label, width=0.8, color= ['blue', 'orange'])

plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Demo Graph- Bar Graph')
plt.show()
