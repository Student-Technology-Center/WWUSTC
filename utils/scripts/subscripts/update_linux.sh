#!/bin/bash

command_exists () {
  type "$1" &> /dev/null 2>&1 ;
}

pythonCommand=''

if command_exists python3 ; then
  pythonCommand='python3'
elif command_exists python ; then
  pythonCommand='python'
elif command_exists py ; then
  pythonCommand='py'
fi

$pythonCommand ../../../manage.py makemigrations --settings=wwustc.$1
$pythonCommand ../../../manage.py migrate --settings=wwustc.$1

# Catching if we're running a dev or local server to prevent script crash
if [ $1 = "settings" ]; then
	$pythonCommand ../../../manage.py collectstatic --noinput --settings=wwustc.$1
fi
