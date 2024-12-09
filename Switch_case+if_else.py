# Пример использования if-else
def check_number(num):
    if num > 0:
        return "Положительное число"
    elif num < 0:
        return "Отрицательное число"
    else:
        return "Ноль"

print(check_number(5))
print(check_number(-3))
print(check_number(0))

# Пример использования switch-case с помощью словаря
def switch_case(value):
    switcher = {
        1: "Первый",
        2: "Второй",
        3: "Третий"
    }
    return switcher.get(value, "Неизвестное значение")

print(switch_case(1))
print(switch_case(4))

# Пример работы со словарями исключений
def get_color_name(color_code):
    color_dict = {
        "R": "Красный",
        "G": "Зеленый",
        "B": "Синий"
    }
    return color_dict.get(color_code, "Неизвестный цвет")

print(get_color_name("R"))
print(get_color_name("Y"))

# Пример использования if-else с списками
def categorize_fruits(fruit):
    if fruit in ["яблоко", "груша", "персик"]:
        return "Косточковые"
    elif fruit in ["банан", "апельсин"]:
        return "Цитрусовые"
    else:
        return "Неизвестный фрукт"

print(categorize_fruits("яблоко"))
print(categorize_fruits("банан"))
print(categorize_fruits("виноград"))
