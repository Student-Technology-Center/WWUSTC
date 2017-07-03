#!/bin/bash
serverIP=$1
port=$2

if [[ $2 -eq 0 ]] ; then
  echo "Usage: ./start.sh <IP> <Port>"
  exit 1
fi

while :
do
	python3 manage.py runserver $1:$2
	echo Restarting in 5 Seconds, Ctrl+C to cancel...
	sleep 1
	
	for i in {4..1}
	do
		echo "$i..."
		sleep 1
	done
done
