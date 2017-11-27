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

$pythonCommand ../../../manage.py makemigrations
$pythonCommand ../../../manage.py migrate
$pythonCommand ../../../manage.py collectstatic --noinput
