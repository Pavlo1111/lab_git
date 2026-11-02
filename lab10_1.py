from numpy import *
import matplotlib.pyplot as plt

x = linspace(1, 4, 1000)                  # 1000 точок між 1 та 4
y = 5 * sin(1 / x) * cos(x**2 + 1 / x)**2 # функція варіанта 21

plt.plot(x, y, 'b-', label='5*sin(1/x)*cos(x^2+1/x)^2')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Графік функції, варіант 21')
plt.legend()
plt.grid(True)

plt.savefig('task1.png', dpi=200)         # зберігаємо в png (до show!)
plt.show()