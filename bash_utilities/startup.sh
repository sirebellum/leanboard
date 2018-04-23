#!/bin/bash

today=`date +%Y-%m-%d.%H:%M:%S`

echo -e "\n-------------------------------------------------" >> /leanboard/logs/ballroom1.py.log
echo $today >> /leanboard/logs/ballroom1.py.log

echo -e "\n-------------------------------------------------" >> /leanboard/logs/ballroom2.py.log
echo $today >> /leanboard/logs/ballroom2.py.log

echo -e "\n-------------------------------------------------" >> /leanboard/logs/bexar.py.log
echo $today >> /leanboard/logs/bexar.py.log

echo -e "\n-------------------------------------------------" >> /leanboard/logs/denman.py.log
echo $today >> /leanboard/logs/denman.py.log

echo -e "\n-------------------------------------------------" >> /leanboard/logs/harris.py.log
echo $today >> /leanboard/logs/harris.py.log

echo -e "\n-------------------------------------------------" >> /leanboard/logs/travis.py.log
echo $today >> /leanboard/logs/travis.py.log

echo -e "\n-------------------------------------------------" >> /leanboard/logs/LED.py.log
echo $today >> /leanboard/logs/LED.py.log

python /leanboard/main.py Ballroom1 >> /leanboard/logs/ballroom1.py.log 2>&1 &
python /leanboard/main.py Ballroom2 >> /leanboard/logs/ballroom2.py.log 2>&1 &
python /leanboard/main.py Bexar >> /leanboard/logs/bexar.py.log 2>&1 &
python /leanboard/main.py Denman >> /leanboard/logs/denman.py.log 2>&1 &
python /leanboard/main.py Harris >> /leanboard/logs/harris.py.log 2>&1 &
python /leanboard/main.py Travis >> /leanboard/logs/travis.py.log 2>&1 &
python /leanboard/main_LED.py >> /leanboard/logs/LED.py.log 2>&1 &
