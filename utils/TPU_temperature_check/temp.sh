#!/bin/bash


while true;
do
  date >> temp.txt;
  cat '/sys/class/thermal/thermal_zone0/temp' >> temp.txt;

done
