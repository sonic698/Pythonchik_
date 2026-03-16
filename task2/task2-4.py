# task_2-4_calories
proteins = float(input("Введите массу белков (г): "))
fats = float(input("Введите массу жиров (г): "))
carbs = float(input("Введите массу углеводов (г): "))
calories = (proteins * 4) + (fats * 9) + (carbs * 4)

print(f"Общая калорийность продукта: {calories:.2f} ккал")

# task_2-4_bmi
weight = float(input("Вес (кг): "))
height = float(input("Рост (м): "))
bmi = weight / (height ** 2)

print("\nОТЧЕТ:")
print(f"Вес:\t{weight:.1f} кг")
print(f"Рост:\t{height:.2f} м")
print(f"ИМТ:\t{bmi:.2f}")

# task_2-4_pharmacy
print("ПРИГОТОВЛЕНИЕ ФИЗРАСТВОРА 0.9%")
print("─" * 35)

vol = float(input("Объем (мл): "))

salt = vol * 0.009
water = vol

print("\n" + "─" * 35)
print("РЕЗУЛЬТАТ:")
print(f"Объем:   {vol:.1f} мл")
print(f"Соль:    {salt:.3f} г")
print(f"Вода:    {water:.1f} мл")
print("─" * 35)

with open("recipe.txt", "w", encoding="utf-8") as f:
    f.write(f"ОТЧЕТ ПО ПРИГОТОВЛЕНИЮ:\n")
    f.write(f"---------------------\n")
    f.write(f"Общий объем: {vol:.1f} мл\n")
    f.write(f"Масса соли:  {salt:.3f} г\n")
    f.write(f"Объем воды:  {water:.1f} мл\n")

print("\nГотово! Рецепт в recipe.txt")