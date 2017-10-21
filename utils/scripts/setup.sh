#!/bin/bash
# Simply clones git repos

if [ -z "$1" ]; then
  echo -e "\e[1m\e[31mUsage: ./setup <prod | true/false>\e[0m"
  exit 1;
fi

prod=$1
LIST_OF_APPS="./utils/scripts/list_of_apps.txt"
LIST_OF_PYTHON_COMMANDS="./utils/scripts/list_of_python_commands.txt"

pushd $(pwd)
cd ../../

cat $LIST_OF_APPS | tr -d '\r' | while read app;
do
  git clone https://github.com/Student-Technology-Center/$app.git

  if $prod; then
    cd $app
    git checkout prod
    cd ..
  else
    cd $app
    git checkout master
    cd ..
  fi
done

cat $LIST_OF_PYTHON_COMMANDS | tr -d '\r' | while read pythonCommand;
do
  echo "Trying $pythonCommand"
  if ! type "$pythonCommand" > /dev/null; then
    continue
  fi

  $pythonCommand manage.py makemigrations
  $pythonCommand manage.py migrate
  $pythonCommand manage.py migrate --run-syncdb
  echo 'yes' | $pythonCommand manage.py collectstatic

  break
done

popd