#!/bin/bash

echo "Поиск всех .conf файлов в директории /etc"

# Используем ls -l и grep с игнорированием регистра
ls -l /etc | grep -i "\.conf"

# Подсчет количества найденных файлов
count=$(ls -l /etc | grep -i "\.conf" | wc -l)

echo "Найдено файлов: $count"
