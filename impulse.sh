#!/bin/bash

if [ $# -ne 2 ]; then
    echo "Ошибка: Недостаточно данных!"
    echo "Использование: ./impulse.sh <имя гена> <уровень экспрессии>"
    exit 1
fi

gene_name=$1
expression_level=$2

echo "Экспрессия гена $gene_name составляет $expression_level единиц"
