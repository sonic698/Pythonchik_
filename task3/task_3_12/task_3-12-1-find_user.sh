#!/bin/bash

echo "Поиск информации о пользователе $USER в файле /etc/passwd"

# Ищем строку с именем текущего пользователя
grep "^$USER:" /etc/passwd

# Проверяем, нашелся ли пользователь
if [ $? -eq 0 ]; then
    echo "Пользователь $USER найден!"
else
    echo "Пользователь $USER не найден в /etc/passwd"
fi
