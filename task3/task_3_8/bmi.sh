#!/bin/bash

echo -n "Вес (кг): "
read weight

echo -n "Рост (м): "
read height

bmi=$(echo "scale=0; $weight / ($height * $height)" | bc)

echo "Ваш BMI: $bmi"
