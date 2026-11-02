import importlib

data = importlib.import_module("3_2_script")   # зчитуємо дані з файлу
dishes = data.dishes
students = data.students

# 1. калорійність усіх страв
for d in dishes:
    print(d["food"], d["calorie_food"])

# 2. меню з найбільшою калорійністю (страва + напій)
m = max(dishes, key=lambda d: d["calorie_food"] + d["calorie_drink"])
print("Макс меню:", m["food"], "+", m["drink"], "=", m["calorie_food"] + m["calorie_drink"])

# 3. меню з найменшою калорійністю
m = min(dishes, key=lambda d: d["calorie_food"] + d["calorie_drink"])
print("Мін меню:", m["food"], "+", m["drink"], "=", m["calorie_food"] + m["calorie_drink"])

# 4. меню з калорійністю менше 300
for d in dishes:
    total = d["calorie_food"] + d["calorie_drink"]
    if total < 300:
        print("Менше 300:", d["food"], "+", d["drink"], "=", total)

# 5. меню з калорійністю більше 500
for d in dishes:
    total = d["calorie_food"] + d["calorie_drink"]
    if total > 500:
        print("Більше 500:", d["food"], "+", d["drink"], "=", total)

# 6. напій з максимальною калорійністю
m = max(dishes, key=lambda d: d["calorie_drink"])
print("Напій макс:", m["drink"], m["calorie_drink"])

# 7. страва з найменшою калорійністю
m = min(dishes, key=lambda d: d["calorie_food"])
print("Страва мін:", m["food"], m["calorie_food"])

# 8. найвищий студент
s = max(students, key=lambda s: s["height"])
print("Найвищий:", s["name"], s["height"])

# 9. наймолодший студент
s = min(students, key=lambda s: s["age"])
print("Наймолодший:", s["name"], s["age"])

# 10. сумарний вік
print("Сумарний вік:", sum(s["age"] for s in students))

# 11. сумарний зріст
print("Сумарний зріст:", sum(s["height"] for s in students))

# 12. найстарший студент
s = max(students, key=lambda s: s["age"])
print("Найстарший:", s["name"], s["age"])

# 13. калорійність усіх напоїв
print("Усі напої:", sum(d["calorie_drink"] for d in dishes))

# 14. калорійність усіх страв
print("Усі страви:", sum(d["calorie_food"] for d in dishes))