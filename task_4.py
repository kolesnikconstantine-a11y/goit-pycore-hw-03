#Імпортування модуля datetime.
from datetime import datetime, timedelta

# Список, кожен елемент якого містить інформацію про ім'я користувача та його день народження
users = [
    {"name": "John Doe", "birthday": "1985.01.03"},
    {"name": "Jane Smith", "birthday": "1990.01.07"},
    {"name": "Zlatan Frank", "birthday": "1995.03.15"},
    {"name": "Adam Levandovsky", "birthday": "1998.03.12"},
    {"name": "Frank Karlsen", "birthday": "1999.04.29"},
    {"name": "Mich Paterson", "birthday": "2004.05.03"}
]

# Функція визначає дні народження на наступні 7 днів включаючи поточний день. 
# Якщо день народження припадає на вихідний, дата привітання переноситься на наступний понеділок.
def get_upcoming_birthdays(users):
    # Створення порожнього списку для зберігання результатів.
    list = []
    # Визначення поточної дати
    today = datetime.today().date() 

    # Aналізування дати народження для кожного користувача
    for user in users:
        # Конвертування дати народження із рядка у datetime об'єкт, без часу.
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        # Визначення дня народження у цьому році
        birthday_this_year = birthday.replace(year=today.year)
                                              
        # Перевірка, чи вже минув день народження в цьому році
        if birthday_this_year < today:
            # Розглядання дати народження на наступний рік
            birthday_next_year = birthday.replace(year=today.year+1)
            # Визначення різниці між днем народження та поточним днем 
            diff_days = birthday_next_year - today
            # Перевірка, чи день народження у найближчи 7 днів, для випадку якщо поточна дата перевірки з 25 грудня до кінця року.
            if diff_days < timedelta(days=7):
                # Отримання номера дня тижня,  Поверне число від 0 (понеділок) до 6 (неділя)
                day_of_week = birthday_this_year.weekday()
                # Перевірка чи день народження у суботу
                if day_of_week == 5:
                    # Перенос дати привітання на два дня(на понеділок)
                    datetime_object = birthday_this_year + timedelta(days=2)
                    congratulation_date = datetime_object.strftime("%Y-%m-%d")
                    
                # Перевірка чи день народження у неділю
                if day_of_week == 6:
                    # Перенос дати привітання на один день(на понеділок)
                    datetime_object = birthday_this_year + timedelta(days=1)
                    congratulation_date = datetime_object.strftime("%Y-%m-%d")
                # Якщо, день народження в інші дні тижня(крім суботи та неділі)
                else:
                    datetime_object= birthday_this_year + timedelta(days=0)
                    congratulation_date = datetime_object.strftime("%Y-%m-%d")
                # Видалення ключа birthday
                del user["birthday"]
                # Додавання ключа congratulation_date
                user.update({"congratulation_date": congratulation_date})
                # Додавання у список ногого словника user, з ключами name та congratulation_date
                list.append(user)

        # Якщо день народження у цьому році ще не наступив
        else:
            # Визначення різниці між днем народження та поточним днем
            diff_days = birthday_this_year - today
            
            # Перевірка, чи день народження у найближчи 7 днів
            if diff_days < timedelta(days=7):
                # Отримання номера дня тижня,  Поверне число від 0 (понеділок) до 6 (неділя)
                day_of_week = birthday_this_year.weekday()
                
                # Перевірка чи день народження у суботу
                if day_of_week == 5:
                    # Перенос дати привітання на два дня(на понеділок)
                    datetime_object = birthday_this_year + timedelta(days=2)
                    congratulation_date = datetime_object.strftime("%Y-%m-%d")
                    
                # Перевірка чи день народження у неділю
                if day_of_week == 6:
                    # Перенос дати привітання на один день(на понеділок)
                    datetime_object = birthday_this_year + timedelta(days=1)
                    congratulation_date = datetime_object.strftime("%Y-%m-%d")
                    
                # Якщо, день народження в інші дні тижня(крім суботи та неділі)
                else:
                    datetime_object= birthday_this_year + timedelta(days=0)
                    congratulation_date = datetime_object.strftime("%Y-%m-%d")
                # Видалення ключа birthday
                del user["birthday"]
                # Додавання ключа congratulation_date
                user.update({"congratulation_date": congratulation_date})
            
                # Додавання у список ногого словника user, з ключами name та congratulation_date
                list.append(user)
    # Повернення списку словників, де кожен словник містить ключі name та congratulation_date, якщо виконуються умови 
    return list

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
