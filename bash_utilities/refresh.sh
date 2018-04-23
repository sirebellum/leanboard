#!/bin/bash

today=`date +%Y-%m-%d.%H:%M:%S`

echo -e "\n-------------------------------------------------" >> /leanboard/logs/refresh.py.log
echo $today >> /leanboard/logs/refresh.py.log

python /leanboard/refresh.py Ballroom1
python /leanboard/refresh.py Ballroom2
python /leanboard/refresh.py Bexar
python /leanboard/refresh.py Denman
python /leanboard/refresh.py Harris
python /leanboard/refresh.py Travis