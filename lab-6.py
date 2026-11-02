text = input("Введіть слова через пропуски, в кінці крапка: ")

text = text.replace(".", "")    # прибираємо крапку в кінці
words = text.split()            # ділимо рядок на слова по пропусках

print("Слова з цифрами:")
for word in words:              # перебираємо кожне слово
    has_digit = False           # поки вважаємо, що цифр у слові немає
    for ch in word:             # перебираємо кожен символ слова
        if ch.isdigit():        # якщо символ це цифра
            has_digit = True
    if has_digit:
        print(word)