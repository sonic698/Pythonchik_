# task_2-7_1
files = ["seq1", "seq2", "seq3", "seq4"]
date = "2026-02-23"

for name in files:
    new_name = f"{name}_{date}.fasta"
    print(new_name)

# task_2-7_2
seq = ["ATATACGCGTA", "CTTCGGNGGA"]

print("ПОСЛЕДОВАТЕЛЬНОСТИ:\n")

for s in seq:
    print("Целиком:", s)
    print("Построчно:")
    
    for letter in s:
        print(letter)
    
    print("-" * 20)  

print("Цикл выполнен")