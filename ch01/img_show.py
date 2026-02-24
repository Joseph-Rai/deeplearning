import matplotlib.pyplot as plt
from matplotlib.image import imread

img = imread(r"C:\Users\ChoiWooseok\Desktop\deeplearning\ch01\cactus.png")

plt.imshow(img)
plt.show()