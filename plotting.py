import matplotlib.pyplot as plt
from csv import reader

def graphiccalc(funcs=(lambda x: x**2), start=-10, end=10, step=1):
    fig = plt.figure()
    for ind in range(len(funcs)):
        func = funcs[ind]
        x = list(range(start, end+1, step))
        y = [func(i) for i in x]
        plt.plot(x, y, label=str(ind))
        plt.xlabel('x')
        plt.ylabel('y')
    plt.show()
    return 

def data(*args):
    for name in args:
        file = open(name)
        plots = reader(file, delimiter=', ')
        x, y = [row[0] for row in plots], [row[1] for row in plots]
        plt.plot(x,y, label='Loaded from file: '+name)
    plt.show()

def test_graphs():
    graphiccalc(funcs=(lambda x: x**2 + 14*x - 8, lambda x: x**2, lambda x: 321*x - 98))
