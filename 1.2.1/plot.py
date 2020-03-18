import numpy as np
import matplotlib.pyplot as plt
t = np.arange(0, 4, 0.1)
plt.plot(t, t, t, t+2, t, t**2)
plt.show()

#plt.show()不可缺少，不然不会出现图像，视频中少了这一部分，代码和编辑器差异，影响不大