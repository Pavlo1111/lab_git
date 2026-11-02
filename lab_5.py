def only_odd_digits(num):
    # перевіряє, чи число складається лише з непарних цифр
    while num > 0:
        digit = num % 10          # беремо останню цифру
        if digit % 2 == 0:        # якщо цифра парна
            return False          # число не підходить
        num = num // 10           # відкидаємо останню цифру
    return True                   # парних цифр не знайшли


def sum_numbers(n):
    # рахує суму всіх n-значних чисел, що містять тільки непарні цифри
    start = 10 ** (n - 1)         # найменше n-значне число (для n=3 це 100)
    end = 10 ** n - 1             # найбільше n-значне число (для n=3 це 999)
    total = 0
    for num in range(start, end + 1):
        if only_odd_digits(num):
            total = total + num
    return total


n = int(input("Введіть n: "))
print("Сума:", sum_numbers(n))