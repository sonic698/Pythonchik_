#!/bin/bash

echo "1. Только имена студентов (первая колонка):"
awk '{print $1}' students.txt

echo "2. Только оценки (вторая колонка):"
awk '{print $2}' students.txt

echo "3. Номер строки и имя студента:"
awk '{print "Строка " NR ": " $1}' students.txt

