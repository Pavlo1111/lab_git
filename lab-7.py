n = int(input("Введіть кількість приладів n: "))

devices = []                      # список усіх приладів
for i in range(n):
    print("Прилад", i + 1)
    name = input("  Назва: ")
    model = input("  Модель: ")
    price = float(input("  Вартість: "))            # число з дробовою частиною
    power = float(input("  Потужність (Вт): "))
    devices.append({"name": name, "model": model, "price": price, "power": power})
    # словник = один прилад, append додає його в список

print("Прилади з потужністю > 1000 Вт:")
cheapest = None                   # найдешевший потужний (поки не знайшли)
for d in devices:
    if d["power"] > 1000:         # потужність більша за 1000
        print(d["name"])          # виводимо назву
        if cheapest is None or d["price"] < cheapest["price"]:
            cheapest = d          # запам'ятовуємо, якщо він перший або дешевший

if cheapest is None:
    print("Немає приладів з потужністю більше 1000 Вт")
else:
    print("Найдешевший серед потужних:", cheapest["name"], cheapest["model"], cheapest["price"])