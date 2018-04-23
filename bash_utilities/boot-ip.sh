#!/bin/bash

today=`date +%Y-%m-%d.%H:%M:%S`

echo -e "\n-------------------------------------------------" >> /leanboard/logs/boot-ip.log
echo $today >> /leanboard/logs/boot-ip.log

echo $HOSTNAME > /home/pi/IP-info
echo -e "\n" >> /home/pi/IP-info
echo $today >> /home/pi/IP-info
echo -e "\n" >> /home/pi/IP-info
ifconfig >> /home/pi/IP-info
cat IP-info | sudo mail -s $HOSTNAME Multimedia@utsa.edu
