#!/bin/bash

if [ -z "$1" ]; then
  echo -e "\e[1m\e[31mUsage: ./setup <prod | true/false> <python>\e[0m"
  exit 1;
fi

$2 setup.py $1

cd ../../
$2 manage.py makemigrations
$2 manage.py migrate
$2 manage.py migrate --run-syncdb
