#!/bin/bash

echo "Анализ использования дискового пространства"

printf "%-20s %-10s %s\n" "Файловая система" "Использовано" "Статус"

df -h | awk 'NR>1 {
    fs=$1
    usage_str=$5

    # Убираем знак процента и преобразуем в число
    gsub(/%/, "", usage_str)
    usage_num = usage_str + 0  # Преобразуем в число

    # Определяем статус
    status = "OK"
    if (usage_num > 90) status = "КРИТИЧНО! (>90%)"

    # Выводим
    printf "%-20s %-10s %s\n", fs, usage_str"%", status
}'
