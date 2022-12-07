import matplotlib.pyplot as plt
import numpy as np
from settings import DATA


def show_plot(filename, title):
    with open(f"/home/mateusz/github/mpis/urny/data/{filename}.txt", "r") as f:
        data = f.readlines()

    i = 0
    for n in range(1000, 100000, 1000):
        x_axis = np.array([n for x in range(50)])
        y_axis = data[i].split("::")[1].split()
        y_axis = [int(item) for item in y_axis]
        avg = np.mean(y_axis)
        if (i == 0):
            plt.scatter(x=x_axis, y=y_axis, s=0.5, c='blue', label="dokładna wartość dla n-urn")
            plt.scatter(x=n, y=avg, s=10, c='red', label="wartośc średnia dla n-urn")
        else:
            plt.scatter(x=x_axis, y=y_axis, s=0.5, c='blue')
            plt.scatter(x=n, y=avg, s=10, c='red')
        i += 1
    plt.title(label=title)
    plt.legend()
    # plt.savefig(title.replace(" ","_"))
    plt.show()


show_plot("B", "Pierwsza kolizja")
show_plot("U", "Liczba pustych urn po wrzuceniu n-kul")
show_plot("L", "Maksymalna liczba kul po wrzuceniu po wrzuceniu n-kul")
show_plot("C", "Minimalna liczba rzutów, po której nie ma pustych urn")
show_plot("D", "Minimalna liczba rzutów, po której w kazdej urnie sa minimum dwie kule")
show_plot("DC", "Liczba rzutów od momentu Cn do Dn")


def iloraz_plot(filename, title, funkcja):
    with open(f"/home/mateusz/github/mpis/urny/data/{filename}.txt", "r") as f:
        data = f.readlines()

    i = 0
    for n in range(1000, 100000, 1000):
        y_axis = data[i].split("::")[1].split()
        y_axis = [int(item) for item in y_axis]
        avg = np.mean(y_axis)
        mianownik = funkcja(n)
        point = avg / mianownik
        if (i == 0):
            plt.scatter(x=n, y=point, s=10, c='green')
        else:
            plt.scatter(x=n, y=point, s=10, c='green')
        i += 1
    plt.title(label=title)
    plt.legend()
    # plt.savefig(title.replace("/","_").replace("*","x"))
    plt.show()


for key, value in DATA.items():
    for j in range(len(value)):
        iloraz_plot(key, key + str(j), value[j])
