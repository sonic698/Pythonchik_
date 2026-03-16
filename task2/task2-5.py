# task_2-5_nucl_count 
print("=== Анализ последовательности ДНК ===\n")

dna = input("Введите последовательность ДНК: ")
dna = dna.upper()

print(f"\nПоследовательность в верхнем регистре: {dna}\n")

a = dna.count('A')
t = dna.count('T')
g = dna.count('G')
c = dna.count('C')
total = len(dna)

print("Подсчёт нуклеотидов:")
print(f"A: {a}")
print(f"T: {t}")
print(f"G: {g}")
print(f"C: {c}")
print(f"\nОбщая длина: {total} нуклеотидов")

if total > 0:
    print("\nПроцентное содержание:")
    print(f"A: {a/total*100:.1f}%")
    print(f"T: {t/total*100:.1f}%")
    print(f"G: {g/total*100:.1f}%")
    print(f"C: {c/total*100:.1f}%")