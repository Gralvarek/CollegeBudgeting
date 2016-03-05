import matplotlib.pyplot as plt
import numpy as np

x_1 = []
d_1 = []

function = 0

demandconst = 5
constraint = 5

dt = .01
x = 0
while x < 10:
    x_1.append(x)
    if(x <= constraint):
        function = demandconst + x**2
        d_1.append(function)
    else:
        function = -((x - constraint)**2) + 30
        d_1.append(function)
    x += dt;


plt.plot(x_1, d_1)
plt.show()