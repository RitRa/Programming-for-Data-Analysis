# Rita Raher 28/09/2018
# matplotlib examples
import matplotlib.pyplot as plt
import numpy as np

plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')

plt.show()

plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.ylabel('some numbers')

plt.show()

plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'b.')
plt.ylabel('some numbers')

plt.show()


x = np.arange(0.0, 10.0, 0.01)
y = 3.0 * x + 1.0

noise = np.random.normal(0.0, 1.0, len(x))

plt.plot(x, y +noise, 'r.')
plt.plot(x, y, 'b-')

plt.show()


plt.plot(x, y +noise, 'c.')
plt.plot(x, y, 'g-')

plt.show()
