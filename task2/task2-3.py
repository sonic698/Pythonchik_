# 1. ВВОД ДАННЫХ
# Функция input() выводит текст и ждет ввода от пользователя.
fio = input("ФИО пациента: ")
symptoms = input("Основные жалобы: ")

# 2. РАБОТА С ФАЙЛОМ
# Менеджер контекста 'with' гарантирует закрытие файла.
# "w" — режим записи (write), очищает файл перед работой.
with open("cartochka_pacienta.txt", "w", encoding="utf-8") as card:
    
    # 3. ФОРМИРОВАНИЕ СТРОКИ И ЗАПИСЬ
    # \t — табуляция (отступ), \n — перенос на новую строку.
    card.write(f"{fio}\t| Жалоба: {symptoms}\n")

# task_2-3_recipe
medium_name = input("Введите название питательной среды: ")
agar_concentration = input("Введите концентрацию агара (%): ")
sterilization_temp = input("Введите температуру стерилизации: ")

with open("recipe.txt", "w", encoding="utf-8") as file:
    file.write(medium_name + "\n")
    file.write("==================\n")
    file.write(f"• Концентрация агара: {agar_concentration}%\n")
    file.write(f"• Температура стерилизации: {sterilization_temp}°C\n")

print("Файл 'recipe.txt' успешно сформирован!")

#task_2-3_sensor
operator_name = input("Введите имя оператора: ")
pressure_value = input("Введите текущее значение датчика давления (Па): ")

with open("sensor_log.txt", "a", encoding="utf-8") as file:
    file.write(f"{operator_name}\t{pressure_value}\n")

print("Данные успешно сохранены в sensor_log.txt")

# task_2-3_lab_journal
researcher = input("ФИО исследователя: ")
date = input("Дата: ")
experiment = input("Название эксперимента: ")
conclusion = input("Вывод: ")

print("\n┌" + "─" * 58 + "┐")
print("│         ЛАБОРАТОРНЫЙ ЖУРНАЛ          │")
print("├" + "─" * 58 + "┤")
print(f"│ ФИО:           {researcher:<40} │")
print(f"│ Дата:          {date:<40} │")
print(f"│ Эксперимент:   {experiment:<40} │")
print("├" + "─" * 58 + "┤")
print(f"│ ВЫВОД: {conclusion:<52} │")
print("└" + "─" * 58 + "┘")

with open("journal.txt", "w", encoding="utf-8") as file:
    file.write("┌" + "─" * 58 + "┐\n")
    file.write("│         ЛАБОРАТОРНЫЙ ЖУРНАЛ          │\n")
    file.write("├" + "─" * 58 + "┤\n")
    file.write(f"│ ФИО:           {researcher:<40} │\n")
    file.write(f"│ Дата:          {date:<40} │\n")
    file.write(f"│ Эксперимент:   {experiment:<40} │\n")
    file.write("├" + "─" * 58 + "┤\n")
    file.write(f"│ ВЫВОД: {conclusion:<52} │\n")
    file.write("└" + "─" * 58 + "┘\n")

print("\n✅ Данные сохранены в journal.txt")