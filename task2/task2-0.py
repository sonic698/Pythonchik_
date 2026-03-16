# task2-0_1
print('Hello World!')

# task2-0_2
print("Фамилия:" "Ишкова", "Имя:" "София", "Группа:" "4731204/50003", "Год:" "2026")

# task2-0_3
print(22, 2, 2026, sep=".")

# task2-0_4
print("Предмет\tОценка\nМатематика\t5\nФизика\t4\nИнформатика\t5")

# task2-0_5
name = "Алёша"
group = 46585
score = 3657583583096
print(f"Студент {name} из группы {group} получил {score} баллов")

# task2-0_6
name = "Ишкова София"
age = 18
city = "Пушкин"
hobby = "Чтение"

with open("output.txt", "w", encoding="utf-8") as файл:
    print("Имя:", name, file=файл)
    print("Возраст:", age, "лет", file=файл)
    print("Город:", city, file=файл)
    print("Хобби:", hobby, file=файл)

print("Файл output.txt создан!")

print("\nСодержимое файла:")
with open("output.txt", "r", encoding="utf-8") as файл:
    print(файл.read())

# task_2-0_creative

print("Добро пожаловать!", end=" ")
print("Рады видеть вас здесь!")
год_обучения = 1
print("\nСтудент", год_обучения, "курса 2026", sep=" ")
print("\n" + "=" * 30)
print("*** Удачи в обучении! ***")
print("=" * 30)
print("\n\tPython")
print("\t  └> Учись программировать")