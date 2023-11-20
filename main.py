import math
import numpy as np
from matplotlib import pyplot as plt
from math import sqrt

data = [0.41, 1.63, -1.53, -0.2, 0.85, 0.09, 1.54, 0.25, 1.24, -0.26, 1.08, 0.42, -0.92, -0.91, 1.25, -0.82, 0.26, 0.96,
        1.57, 0.72]

print("Исходные данные:")
print(data)
print()

print("Вариационный ряд: ")
print(sorted(data))
print()

print("Экстремальные значения:")
print(f"минимум: {min(data)}, максимум: {max(data)}, размах: {max(data) - min(data)}")
print()

diversity = [(i, data.count(i)) for i in set(data)]
n = len(diversity)
m = sum([i * j for i, j in diversity]) / n
d = sum([((i - m) ** 2) * j for i, j in diversity]) / n
print(f"Выборочное среднее: {m}")
print(f"Выборочная дисперсия: {d}")
print(f"Среднеквадратическое отклонение: {sqrt(d)}")
print(f"Исправленное выборочное среднеквадратичное отклонение: {sqrt(n * d / (n - 1))}")


# Эмпирическая функция распределения
def f(start, end):
    return sum([j for i, j in diversity if start <= i < end]) / n


x = np.linspace(min(data), max(data), 100)
y = [f(min(data), i) for i in x]
plt.plot(x, y, color='blue')
plt.title("Эмпирическая функция распределения")
plt.show()


# Полигон приведенных частот группированной выборки
h = (max(data) - min(data)) / (1 + math.log2(n))
x_start = min(data) - h / 2
x = np.arange(x_start, max(data), h)
y = [f(i, i + h) for i in x]
plt.plot(x, y)
plt.title("Полигон приведенных частот группированной выборки")
plt.show()

# Гистограмма приведенных частот группированной выборки
h = (max(data) - min(data)) / (1 + math.log2(n))
x_start = min(data) - h / 2
x = np.arange(x_start, max(data), h)
y = [f(i, i + h) for i in x]
plt.bar(x, y)
plt.title("Полигон приведенных частот группированной выборки")
plt.show()
