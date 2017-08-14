#!/bin/bash
# Simply clones git repos

if [ -z "$1" ]; then
  echo -e "\e[1m\e[31mUsage: ./setup <prod | true/false>\e[0m"
  exit 1;
fi

prod=$1

apps=(
  hour_manager
  evaluations
  lfp_scheduler
)

for item in ${apps[*]}
do
  git clone https://github.com/Student-Technology-Center/$item.git

  if $prod; then
    cd $item
    git checkout prod
    cd ..
  else
    cd $item
    git checkout master
    cd ..
  fi
done

pythonCommands=(
  python3
  py
  python
)

for pythonCommand in ${pythonCommands[*]}
do
  echo "Trying $pythonCommand"
  if ! type "$pythonCommand" > /dev/null; then
    continue
  fi

  $pythonCommand manage.py makemigrations
  $pythonCommand manage.py migrate
  echo 'yes' | $pythonCommand manage.py collectstatic

  break
done
