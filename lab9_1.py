import os
import time

# 1. повний шлях і список файлів поточного каталогу
print("1. Поточний каталог:", os.getcwd())
print("   Файли:", os.listdir('.'))

# 2. розмір файла в байтах (беремо сам цей скрипт)
print("2. Розмір файла lab9_1.py:", os.path.getsize('lab9_1.py'), "байт")

# 3. пошук файлів за шаблоном (усі, що закінчуються на .py)
print("3. Файли .py у каталозі:")
for name in os.listdir('.'):
    if name.endswith('.py'):
        print("  ", name)

# 4. два текстові файли: копіювання, читання, видалення першого
f = open('first.txt', 'w', encoding='utf-8')     # перший файл з текстом
f.write('Це довільний текст у першому файлі.')
f.close()
f = open('second.txt', 'w', encoding='utf-8')    # другий файл порожній
f.close()

with open('first.txt', 'r', encoding='utf-8') as f1:
    data = f1.read()                              # читаємо з першого
with open('second.txt', 'w', encoding='utf-8') as f2:
    f2.write(data)                                # пишемо в другий

with open('second.txt', 'r', encoding='utf-8') as f2:
    print("4. Вміст second.txt:", f2.read())       # читаємо з другого

os.remove('first.txt')                            # видаляємо перший файл
print("   first.txt існує?", os.path.exists('first.txt'))

# 5. поточна дата й час
print("5. Зараз:", time.ctime())

# 6. скільки днів і років минуло з початку епохи Unix
seconds = time.time()          # секунд від 01.01.1970
days = seconds / 86400         # у добі 86400 секунд
years = days / 365             # 1 рік = 365 днів
print("6. Днів:", int(days), " Років:", round(years, 2))