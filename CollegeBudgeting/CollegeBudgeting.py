import matplotlib.pyplot as plt
from Function import Function

def main():
    x_ = []
    d_ = []
    dt = 0.01
    
    func = Function()
    x = 0
    while x < 10:
        x_.append(x)
        function = func.savings(x, 3)
        d_.append(function)
        x += dt;


    plt.plot(x_, d_)
    plt.show()


main()

