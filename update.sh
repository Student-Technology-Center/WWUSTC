#!/bin/bash

if [ -z "$1" ]; then
  echo -e "\e[1m\e[31mUsage: ./setup <prod | true/false>\e[0m"
  exit 1;
fi

prod=$1
LIST_OF_APPS="list_of_apps.txt"
LIST_OF_PYTHON_COMMANDS="list_of_python_commands.txt"

# restart is a variable where if set to true, at the end of this script, the django server will restart
restart=false


# Check-repo is a function that checks with upstream to see if an update is needed.
# If so, it'll update that repo and also set $restart to true
check-repo ()
{
  git remote update

  UPSTREAM=${1:-'@{u}'}
  LOCAL=$(git rev-parse @)
  REMOTE=$(git rev-parse "$UPSTREAM")
  BASE=$(git merge-base @ "$UPSTREAM")

  if [[ $LOCAL = $REMOTE ]]; then echo "Up-to-date";
  elif [[ $LOCAL = $BASE ]]; then 
    echo "Update found, pulling and staging the django restart...";
    git pull
    restart=true
  elif [[ $REMOTE = $BASE ]]; then echo "Local files have been edited.";
  else echo "Diverged";
  fi

  echo "-----------------------"
  echo ""
}

echo ""

# We start to iterate through the apps...
cat $LIST_OF_APPS | tr -d '\r' | while read app;
do
  echo "Updating $item..."
  cd $app
  check-repo
  cd ..
done

# Same thing as before, just with the main repo
echo "Updating WWU STC Django Project..."
check-repo

pythonCommands=(
  python3
  python
  py
)

# Sends the restart command to django if needed
if $restart; then
  cat $LIST_OF_PYTHON_COMMANDS | tr -d '\r' | while read pythonCommand;
  for command in ${pythonCommands[*]}
  do
    if ! type "$command" > /dev/null; then
      continue
    fi

    $command manage.py makemigrations
    $command manage.py migrate
    echo 'yes' | $command manage.py collectstatic

    break
  done
fi

# I hate myself
if $prod; then
  #pip3 install "git+https://github.com/Student-Technology-Center/django-wiki.git@prod"
else
  #pip3 install "git+https://github.com/Student-Technology-Center/django-wiki.git"
fi
