#!/bin/bash

echo "Создаем файлы..."

# Создаем 10 файлов
for i in {1..10}; do
    touch "test$i.txt"
    echo "Создан test$i.txt"
done

echo ""
echo "Удаляем файлы в обратном порядке..."

# Удаляем в обратном порядке
i=10
while [ $i -ge 1 ]; do
    rm "test$i.txt"
    echo "Удален test$i.txt"
    i=$((i - 1))
done

echo ""
echo "Готово!"
