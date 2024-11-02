import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x + 2 * np.sin(x) + np.cos(3 * x)

def parabola_approximation(a, b, c):
    x_vals = np.array([a, b, c])
    y_vals = np.array([f(a), f(b), f(c)])
    coeffs = np.polyfit(x_vals, y_vals, 2)
    return np.poly1d(coeffs)

def plot_function_with_parabola(a, b, current_c, parabola_fn, iteration):
    x_vals = np.linspace(a, b, 1000)
    y_vals = f(x_vals)

    plt.plot(x_vals, y_vals, label='f(x) = x + 2sin(x) + cos(3x)', color='blue')

    y_parabola = parabola_fn(x_vals)
    plt.plot(x_vals, y_parabola, '--', label=f'Аппроксимация параболой на итерации {iteration}', color='orange')

    plt.scatter(current_c, f(current_c), color='red', label=f'Итерация {iteration}, c = {current_c:.4f}')

    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)

    plt.title('График функции и параболы на каждой итерации')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid(True)
    plt.legend()
    plt.show()

def parabola_method(a, b, eps=1e-5):
    max_iter = 1000

    for k in range(max_iter):
        fa, fb = f(a), f(b)
        c = (a * fb - b * fa) / (fb - fa)
        fc = f(c)

        parabola_fn = parabola_approximation(a, b, c)

        print(f"Итерация {k+1}: c = {c:.6f}, f(c) = {fc:.6f}, точность = {eps}")
        plot_function_with_parabola(a, b, c, parabola_fn, k+1)

        if abs(fc) < eps:
            print(f"Решение найдено: x = {c:.6f}, f(x) = {fc:.6f}, количество итераций = {k+1}, точность = {eps}")
            return c, k+1

        if np.sign(fa) * np.sign(fc) < 0:
            b = c
        else:
            a = c

    print(f"Решение не найдено за {max_iter} итераций, точность = {eps}")
    return None, max_iter

a, b = -5, 5

parabola_method(a, b)
