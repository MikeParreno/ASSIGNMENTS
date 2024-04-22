import matplotlib.pyplot as plt
import numpy as np


ass=int(input('Enter Number: '))

if ass ==1:
    x = np.linspace(-5, 5, 100)
    y = x**2 - 10
    plt.plot(x, y)

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Plot of x^2 - 10')

    plt.show()    
elif ass ==2:
    x = np.linspace(-5, 5, 100)
    y = x**3 - x - 100
    plt.plot(y, color="m")
    plt.axhline(y=0, color="c")
    plt.axvline(x=0, color="k")
    plt.show()
elif ass == 3:
        x = np.linspace(-5, 5, 100)
        y = x**10 - x**8 + x**2 - 8
        plt.plot(y, color="m")
        plt.axhline(y=0, color="c")
        plt.axvline(x=0, color="k")
        plt.show()
elif ass == 4:
        x = np.linspace(-5, 5, 100)
        y = x**4 + x**3 + x**2 + x + 1
        plt.plot(y, color="m")
        plt.axhline(y=0, color="c")
        plt.axvline(x=0, color="k")
        plt.show()
elif ass ==5:
        x = np.linspace(-5, 5, 100)
        y =(x**2 + x + 10)/(2*x)
        plt.plot(y, color="m")
        plt.axhline(y=0, color="c")
        plt.axvline(x=0, color="k")
        plt.show()
elif ass == 6:
        x = np.linspace(-5, 5, 100)
        y =(np.sin(x))/(3*x)
        plt.plot(y, color="m")
        plt.axhline(y=0, color="c")
        plt.axvline(x=0, color="k")
        plt.show()
elif ass == 7:
    x = np.linspace(-5, 5, 100)
    y = x**3 + 2*x**2 - 10*x + 3
    plt.plot(y, color="m")
    plt.axhline(y=0, color="c")
    plt.axvline(x=0, color="k")
    plt.show()
elif ass == 8:
    x = np.linspace(-5, 5, 100)
    y =(np.cos(x))/(5*x)
    plt.plot(y, color="m")
    plt.axhline(y=0, color="c")
    plt.axvline(x=0, color="k")
    plt.show()
elif ass == 9:
    x = np.linspace(-5, 5, 100)
    y =(x**3)/(2*x) - 10*x
    plt.plot(y, color="m")
    plt.axhline(y=0, color="c")
    plt.axvline(x=0, color="k")
    plt.show()
elif ass ==10:
    x = np.linspace(-5, 5, 100)
    y =(x+2)*(x+3)*(x-4)
    plt.plot(y, color="m")
    plt.axhline(y=0, color="c")
    plt.axvline(x=0, color="k")
    plt.show()
print(ass)