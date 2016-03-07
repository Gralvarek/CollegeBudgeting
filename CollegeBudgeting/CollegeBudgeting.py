import matplotlib.pyplot as plt
from Function import Function

def main():
    x_ = []
    d_ = []
    dt = 0.01
    
    func = Function(5)
    x = 0
    while x < 10:
        x_.append(x)
        if(x <= func.constraint):
            function = func.savings(x, '1', 5, 30)
            d_.append(function)
        else:
            function = func.savings(x, '2', 5, 30)
            d_.append(function)
        x += dt;


    plt.plot(x_, d_)
    plt.show()


main()

