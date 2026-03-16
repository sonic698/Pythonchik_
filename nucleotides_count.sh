#!/bin/bash

echo "ПОДСЧЕТ НУКЛЕОТИДОВ В FASTA"

# Заголовок таблицы
echo "Файл         A   T   G   C"

# Перебираем все fasta файлы
for file in *.fasta; do
    # Проверяем, что файл существует
    if [ ! -f "$file" ]; then
        continue
    fi

    # Проверяем, не пустой ли файл
    if [ ! -s "$file" ]; then
        echo "$file - пустой файл"
        continue
    fi

    # Получаем последовательность (убираем строки с >)
    sequence=$(grep -v "^>" "$file" | tr -d '\n')

    # Считаем нуклеотиды
    a=$(echo "$sequence" | grep -o "A" | wc -l)
    t=$(echo "$sequence" | grep -o "T" | wc -l)
    g=$(echo "$sequence" | grep -o "G" | wc -l)
    c=$(echo "$sequence" | grep -o "C" | wc -l)

    echo "$file   $a   $t   $g   $c"
done
