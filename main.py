import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

path = input("path?")
image = Image.open(path)
image = np.array(image)
print(np.shape(image))
plt.imshow(image)
plt.show()



bounds_0_x = [303, 317]
bounds_0_y = [783, 866]
#bounds_1_x = [499, 502]
#bounds_1_y = [507, 735]

sample0 = image[bounds_0_y[0]:bounds_0_y[1], bounds_0_x[0]:bounds_0_x[1], :]
#sample1 = image[bounds_1_y[0]:bounds_1_y[1], bounds_1_x[0]:bounds_1_x[1], :]
plt.imshow(sample0)
plt.show()

sum0 = np.sum(np.sum(sample0, axis=2), axis=1)
#sum1 = np.sum(np.sum(sample1, axis=2), axis=1)
plt.plot(np.arange(bounds_0_y[1]-bounds_0_y[0]), sum0, c='blue')
#plt.plot(np.arange(bounds_0_y[1]-bounds_0_y[0]), sum1, c='red')
plt.show()
