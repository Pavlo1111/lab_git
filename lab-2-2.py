n = int(input("Введіть натуральне число n: "))

S = 0
for i in range(n, 2 * n + 1):
    S = S + i ** 2

print("S =", S)