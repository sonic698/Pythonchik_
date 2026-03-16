#!/bin/bash

echo "1. Названия товаров (вторая колонка):"
awk -F "," '{print $2}' data.csv

echo "2. Товары дороже 20:"
awk -F "," '$3 > 20 {print $2 " - " $3 " руб."}' data.csv

echo "3. Общая стоимость всех товаров:"
total=$(awk -F "," '{sum += $3} END {print sum}' data.csv)
echo "Сумма: $total руб."

