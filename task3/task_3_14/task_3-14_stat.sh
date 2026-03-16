#!/bin/bash

echo "Статистика по оценкам студентов"
# Сумма всех оценок
sum=$(awk '{sum += $2} END {print sum}' students.txt)
echo "Сумма всех оценок: $sum"

# Средняя оценка
avg=$(awk '{sum += $2; count++} END {print sum/count}' students.txt)
echo "Средняя оценка: $avg"

# Максимальная оценка
max=$(awk 'NR==1 {max=$2} $2 > max {max=$2} END {print max}' students.txt)
echo "Максимальная оценка: $max"
