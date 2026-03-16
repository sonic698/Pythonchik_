#!/bin/bash

echo "Замена пробелов на табуляцию в файле sequences.txt"

echo "Исходный файл:"
cat sequences.txt

# Выполняем замену пробелов на табуляцию
sed -i 's/ /\t/g' sequences.txt

echo "После замены:"
cat -T sequences.txt
echo "Замена выполнена!"
