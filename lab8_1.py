import csv

# 1. записуємо рядок у файл
test1 = 'Test variable to write to file'
f = open('tests.txt', 'w')
f.write(test1)
f.close()

# 2. читаємо файл назад
f = open('tests.txt', 'r')
test2 = f.read()
f.close()

# 3. порівнюємо
print(test1 == test2)            # True, якщо рядки однакові

# 4. створюємо painters.csv
f = open('painters.csv', 'w', encoding='utf-8')
f.write('author,canvas\n')
f.write('Vincent Willem van Gogh,"Vase with sunflowers"\n')
f.write('Rembrandt Harmenszoon van Rijn,"Aristotle"\n')
f.write('Leonardo da Vinci,"Selfportrait"\n')
f.close()

# 5. читаємо через DictReader
f = open('painters.csv', 'r', encoding='utf-8')
painters = list(csv.DictReader(f))
f.close()
print(painters)

# 6. створюємо imdb.csv зі списку словників
imdb = [
    {'title': 'Lord of the Rings: Two towers', 'year': 2002, 'rating': 8.7},
    {'title': 'Matrix', 'year': 1999, 'rating': 8.7},
    {'title': 'Interstellar', 'year': 2014, 'rating': 8.5},
    {'title': 'Back to the Future', 'year': 1985, 'rating': 8.5},
    {'title': 'Logan: Wolverine', 'year': 2017, 'rating': 8.1},
]
f = open('imdb.csv', 'w', newline='', encoding='utf-8')
w = csv.DictWriter(f, fieldnames=['title', 'year', 'rating'])
w.writeheader()                  # записує рядок із назвами колонок
w.writerows(imdb)                # записує всі словники
f.close()