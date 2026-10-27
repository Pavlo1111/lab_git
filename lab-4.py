n = int(input("Введіть розмір матриці n: "))

# створюємо матрицю: список, у якому лежать рядки (теж списки)
matrix = []
for i in range(n):
    row = []                      # новий порожній рядок
    for j in range(n):
        x = int(input(f"Елемент [{i}][{j}]: "))
        row.append(x)             # append додає елемент в кінець списку
    matrix.append(row)            # додаємо готовий рядок до матриці

print("Початкова матриця:")
for i in range(n):
    for j in range(n):
        print(f"{matrix[i][j]:5}", end="")   # end="" - не переходити на новий рядок
    print()                                   # перехід на новий рядок після кожного рядка матриці

# проходимо по кожному стовпцю j
for j in range(n):
    imin = 0                      # номер рядка, де лежить мінімум (поки вважаємо, що в 0-му)
    for i in range(1, n):
        if matrix[i][j] < matrix[imin][j]:
            imin = i              # знайшли менший елемент, запам'ятовуємо його рядок

    # міняємо місцями мінімум стовпця та елемент головної діагоналі [j][j]
    tmp = matrix[imin][j]
    matrix[imin][j] = matrix[j][j]
    matrix[j][j] = tmp

print("Матриця після обміну:")
for i in range(n):
    for j in range(n):
        print(f"{matrix[i][j]:5}", end="")
    print()