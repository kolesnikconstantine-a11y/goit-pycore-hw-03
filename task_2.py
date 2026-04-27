# Використання модуля random для генерації випадкових чисел.
import random

def get_numbers_ticket(min, max, quantity):
    # Перевірка заданих параметрів
    if min >= 1 and max <= 1000 and quantity < max and quantity > min:
        # Формування списка numbers, з урахування min та max 
        numbers = []
        index = 1
        while index <= max:
            numbers.append(index)
            index +=1
    
        # Використання методу sample(), який повертає список довжиною quantity з унікальними елементами, вибраними випадково з numbers.
        chosen_numbers = random.sample(numbers, quantity)
        # Використання методу sorted(), який повертає новий відсортований об'єкт
        sorted_num = sorted(chosen_numbers)
        # Функиція повертає список випадково вибраних, відсортованих чисел. 
        return sorted_num
    else:
        # Повернення пустого списка, якщо параметри не відповідають заданим обмеженням
        return []



lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)


