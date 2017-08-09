#!/bin/bash

python3 manage.py makemigrations

if [ $? -eq 127 ]
then
    python_command="py"
    py manage.py makemigrations
else
    python_command="python3"
fi

$python_command manage.py migrate

while :
do

    $python_command manage.py runserver --settings=wwustc.dev-settings
	echo Restarting in 5 Seconds, Ctrl+C to cancel...
	sleep 1
	
	for i in {4..1}
	do
		echo "$i..."
		sleep 1
	done
done
