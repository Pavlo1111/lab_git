import matplotlib.pyplot as plt

text = "Привіт! Як справи? Все добре. Не знаю... Чому так? Ура! Сьогодні гарна погода. Подивимось..."
# можна вставити будь-який свій текст

ellipsis = text.count('...')                  # речення з трикрапкою
normal = text.count('.') - 3 * ellipsis       # крапки без трикрапок
question = text.count('?')                    # питальні
exclam = text.count('!')                      # окличні

names = ['Звичайні', 'Питальні', 'Окличні', 'Трикрапка']
values = [normal, question, exclam, ellipsis]

plt.bar(names, values, color=['blue', 'green', 'red', 'orange'])
plt.ylabel('Кількість речень')
plt.title('Типи речень у тексті')

plt.savefig('task3.png', dpi=200)
plt.show()