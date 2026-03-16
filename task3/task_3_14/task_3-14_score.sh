#!/bin/bash

echo "1. Студенты с оценкой ВЫШЕ 80:"
awk '$2 > 80 {print $1 " - " $2}' students.txt

echo "2. Студенты с оценкой НИЖЕ 70:"
awk '$2 < 70 {print $1 " - " $2}' students.txt

echo "3. Первая строка файла:"
awk 'NR==1 {print "Имя: " $1 ", Оценка: " $2}' students.txt
