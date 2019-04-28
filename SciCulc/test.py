import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0.0, 10.0, 100)
y = np.sin(x)

print(f"x={x}")
print(f"y={y}")
plt.loglog(x,y**2,'r-o')
plt.show()
