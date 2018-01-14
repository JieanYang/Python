import matplotlib.pyplot as plt

plt.figure()

# subplot(rows, columns, position)
plt.subplot(2, 1, 1)
plt.plot([0,1],[0,1])
plt.subplot(2, 3, 4)
plt.plot([0,1],[0,2])
plt.subplot(235)
plt.plot([0,1],[0,3])
plt.subplot(236)
plt.plot([0,1],[0,4])


plt.show()