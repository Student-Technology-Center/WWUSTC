#!/bin/bash
while :
do
	python3 manage.py runserver localhost:8000
	echo Restarting in 5 Seconds, Ctrl+C to cancel...
	sleep 1
	
	for i in {4..1}
	do
		echo "$i..."
		sleep 1
	done
done
