NICKNAME = "underham2ter"
import numpy as np
import matplotlib.pyplot as plt


def null_vec():
    a = np.array([0 if i != 4 else 5 for i in range(10)])
    return a


print(null_vec())


def reverse_vec(v):
    v_rev = [v[-i] for i in range(1, len(v)+1)]
    return v_rev


print(reverse_vec([1, 2, 3]))


def matrix():
    m = [[i for i in range(j, j+3)] for j in range(0, 7, 3)]
    return m


print(matrix())


def checkerboard(w, b):
    """Создает матрицу по принципу шахматной доски.
    Parameters
    ----------
    w: Символ, обозначающий белую клетку
    b: Символ, обозначающий черную клетку

    Returns
    -------
    m: Матрица 8х8.
    """
    m = [[w if (i+j)%2==0 else b for i in range(0, 8)] for j in range(0, 8)]
    return m


print(checkerboard('w', 'b'))


def cartesian_to_polar(c):
    """Переводит массив, состоящий из 10 пар координат xy
    в массив координат r phi.

    Parameters
    ----------
    c: Array of int.
    Массив размерами 10х2, каждая строка -- декартовы координаты точки.

    Returns
    -------
    p: Array of int.
    Аналогичный массив из пар полярных координат. В первом столбике r.
    """
    p = [[np.sqrt(x**2 + y**2), np.arctan2(y, x)] for x, y in c]
    return p


print(cartesian_to_polar([[3, 2], [5, 3], [0, 1], [-1, -1]]))


def make_curve(n, a):
    """Функция возвращает массив nх2, содержащий n пар
    декартовых координат точек кривой Паскаля"""
    phi = np.linspace(0, 2*np.pi, n)
    p = [[a+np.cos(i), i] for i in phi]
    xy = [[r * np.cos(phi), r * np.sin(phi)] for r, phi in p]
    return xy


N = 50
A = 1
m = make_curve(N, A)

for a in range(1, 5):
    color = [str(a / 255.)]
    M = np.array(make_curve(N, a))
    x = [M[i][0] for i in range(len(M))]
    y = [M[i][1] for i in range(len(M))]
    plt.plot(x, y, color)
plt.show()
