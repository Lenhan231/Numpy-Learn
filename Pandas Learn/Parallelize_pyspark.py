import matplotlib.pyplot as plt
 
# Data
x = [1, 2, 3, 4, 5]
y1, y2 = [10, 20, 15, 25, 30], [5, 15, 10, 20, 25]
 
# Area Chart
plt.fill_between(x, y1, y2, color='skyblue', alpha=0.4, label='Area 1-2')
plt.plot(x, y1, label='Line 1', marker='o')
plt.plot(x, y2, label='Line 2', marker='o')
 
# Labels and Title
plt.xlabel('X-axis'), plt.ylabel('Y-axis'), plt.title('Area Chart Example')
 
# Legend and Display
plt.legend(), plt.show()