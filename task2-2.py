# task_2-2_1
curse_name = "Информатика"
etap_nomber = 1
zadach = "много"

print(f"Название курса: {curse_name} \nНомер текущего этапа: {etap_nomber} \nКоличество выполненных задач: {zadach}")

# task_2-2_2
user_input = input("Введите текст: ")
processed_input = user_input.upper()

print(user_input, processed_input, sep=" -> ")

# task_2-2_3
device_name = "Микроскоп"
inventory_number = "М-2023-045"
is_working = "исправен"
quantity = 3

print("Название\tИнвентарный номер\tСостояние\tКоличество")
print("-" * 60)
print(device_name, "\t", inventory_number, "\t\t", is_working, "\t", quantity, sep="")

# task_2-2_inventory_control
reagent_name = input("Введите название нового реактива:")
reagent_quantity = int(input("Введите количество:"))

print(f"Реактив {reagent_name} поступил на склад в количестве {reagent_quantity} шт.")

with open("inventory.txt", "a", encoding="utf-8") as file:
    file.write(f"Реактив {reagent_name} поступил на склад в количестве {reagent_quantity} шт.\n")

print("Данные также сохранены в файл inventory.txt")