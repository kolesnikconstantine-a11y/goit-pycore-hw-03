#Імпортування модуля datetime.
import datetime

# Функція приймає один параметр: date — рядок, що представляє дату у форматі 'РРРР-ММ-ДД'
def get_days_from_today(date):

    try:
        # Перетворення рядка в об'єкт datetime
        datetime_object = datetime.datetime.strptime(date, "%Y-%m-%d")
   
        # Отримання поточної дати, використовуючи datetime.today().
        now = datetime.datetime.today()

        # Розрахунок різниці між поточною датою та заданою датою.
        days_diff = now - datetime_object
        # Поверненя тільки днів, ігноруючи час (години, хвилини, секунди).
        return days_diff.days

    # Обробка винятка, якщо неправильний формат вхідних даних
    except ValueError:
        print(f"Date {date} does not match format '%Y-%m-%d")

# Функція повертає ціле число, яке вказує на кількість днів від заданої дати до поточної.
res = get_days_from_today("2028-11-01")
print(res)

