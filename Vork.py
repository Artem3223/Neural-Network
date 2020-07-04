import matplotlib.pyplot as plt
import numpy as np
from scipy import misc

i = misc.ascent()

i_transformed = np.copy(i)
size_x = i_transformed.shape[0]
size_y = i_transformed.shape[1]

filter = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]
weight = 1

new_x = int(size_x / 2)
new_y = int(size_y / 2)
newImage = np.zeros((new_x, new_y))

new_x = int(size_x / 2)
new_y = int(size_y / 2)
newImage = np.zeros((new_x, new_y))
for x in range(0, size_x, 2):
    for y in range(0, size_y, 2):
        pixels = [i_transformed[x, y], i_transformed[x + 1, y], i_transformed[x, y + 1], i_transformed[x + 1, y + 1]]
        pixels.sort(reverse=True)
        newImage[int(x / 2), int(y / 2)] = pixels[0]

plt.gray()
plt.grid(False)
plt.imshow(i_transformed)
plt.show()
