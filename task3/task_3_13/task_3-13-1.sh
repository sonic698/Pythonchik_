#!/bin/bash

echo "Замена пути к базе данных в файле settings.php"

echo "Исходный файл:"
grep "db_data_path" settings.php

# Выполняем замену с разделителем '|'
sed -i 's|/var/lib/mysql/data|/mnt/ssd/mysql|g' settings.php

echo "После замены: db_data_path" settings.php
echo "Замена выполнена!"
