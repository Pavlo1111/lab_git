from datetime import datetime, timedelta

# ---------- Завдання 2.1 ----------
now = datetime.now()
f = open('today.txt', 'w', encoding='utf-8')
f.write(now.strftime('%Y-%m-%d %H:%M:%S'))        # записуємо дату й час рядком
f.close()

with open('today.txt', 'r', encoding='utf-8') as f:
    today_string = f.read()                       # читаємо назад

d = datetime.strptime(today_string, '%Y-%m-%d %H:%M:%S')   # розбираємо рядок
print("Рік:", d.year)
print("Місяць:", d.month)
print("День:", d.day)
print("Година:", d.hour)
print("Хвилина:", d.minute)
print("Секунда:", d.second)

# ---------- Завдання 2.2 ----------
happy = datetime(2005, 9, 12)                     # ЗАМІНІТЬ на свою дату народження: рік, місяць, день

days_of_week = ['понеділок', 'вівторок', 'середа', 'четвер',
                "п'ятниця", 'субота', 'неділя']
weekday = days_of_week[happy.weekday()]           # weekday() дає номер дня: 0 = понеділок

date_13330 = happy + timedelta(days=13330)        # дата через 13 330 днів

f = open('birthday.txt', 'w', encoding='utf-8')
f.write("Яка дата вашого народження? " + happy.strftime('%d.%m.%Y') + "\n")
f.write("У який день тижня ви народилися? " + weekday + "\n")
f.write("Коли вам буде (або вже було) 13330 днів? " + date_13330.strftime('%d.%m.%Y') + "\n")
f.close()

print(open('birthday.txt', encoding='utf-8').read())