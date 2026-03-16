#!/bin/bash

echo "Анализ использования дискового пространства"

# Выводим заголовок
printf "%-20s %-10s %s\n" "Файловая система" "Использовано" "Статус"

# Анализируем вывод df -h, пропускаем заголовок
df -h | awk 'NR>1 {
    fs=$1
    usage=$5
    gsub(/%/, "", usage)

    status="OK"
    if (usage > 90) status="КРИТИЧНО!"

    printf "%-20s %-10s %s\n", fs, usage"%", status
}'
