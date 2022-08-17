#!/bin/bash


while true;
do
  date >> tpu_temperature_check.txt;
  cat '/sys/class/thermal/thermal_zone0/temp' >> tpu_temperature_check.txt;

done
