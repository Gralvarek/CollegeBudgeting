import matplotlib.pyplot as plt
from Function import Function

def main():
    x_ = []
    d_1 = []
    d_2 = []
    dt = 0.01
    
    func = Function()
    x = 0
    while x < 10:
        x_.append(x)
        d_1.append(func.savings(x, 30))
        d_2.append(func.transportation(x, 5, 5, 30))
        x += dt;


    plt.plot(x_, d_1)
    plt.plot(x_, d_2)
    plt.show()


main()

