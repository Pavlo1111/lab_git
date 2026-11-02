import matplotlib.pyplot as plt

text = "Python це проста та потужна мова програмування. Вона підходить для аналізу даних, створення сайтів і автоматизації."
# можна вставити будь-який свій текст

counts = {}                               # словник: літера -> скільки разів
for ch in text.lower():                   # lower() щоб А і а рахувались разом
    if ch.isalpha():                      # беремо лише літери
        if ch in counts:
            counts[ch] += 1
        else:
            counts[ch] = 1

letters = sorted(counts)                  # літери за алфавітом
values = [counts[l] for l in letters]     # їх кількості

plt.bar(letters, values)
plt.xlabel('Літера')
plt.ylabel('Кількість')
plt.title('Частота появи літер')

plt.savefig('task2.png', dpi=200)
plt.show()