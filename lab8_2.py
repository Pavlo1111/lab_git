# створюємо файл learning_python.txt
f = open('learning_python.txt', 'w', encoding='utf-8')
f.write('In Python you can write programs.\n')
f.write('In Python you can work with files.\n')
f.write('In Python you can analyze data.\n')
f.close()

# пункт 3: читаємо файл і зберігаємо рядки в список
lines = []
with open('learning_python.txt', 'r', encoding='utf-8') as f:
    for line in f:
        lines.append(line.strip())

# вивід списку поза блоком with
print("Пункт 3:")
print(lines)
for line in lines:
    print(line)

# пункт 4: заміна Python на C
print("Пункт 4:")
with open('learning_python.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line.strip().replace('Python', 'C'))