#!/bin/bash

restartServer=false

update-repo ()
{
  UPSTREAM=${1:-'@{u}'}
  LOCAL=$(git rev-parse @)
  REMOTE=$(git rev-parse "$UPSTREAM")
  BASE=$(git merge-base @ "$UPSTREAM")

  if [ $LOCAL = $REMOTE ]; then
      echo "Up-to-date"
  elif [ $LOCAL = $BASE ]; then
      echo "Update found, pulling..."
      git pull
      restartServer=true
      cd ..
  elif [ $REMOTE = $BASE ]; then
      echo "Local files have been edited."
  else
      echo "Diverged"
  fi
}

if [ ! -d cas/ ]
then
  echo "Cloning Django-Cas"
  git clone https://github.com/kstateome/django-cas.git
  mv django-cas/cas/ cas/
  rm -rf django-cas/
  restartServer=true
fi

if [ ! -d hour_manager/ ]
then
  echo "Cloning Hour Manager"
  git clone https://github.com/Student-Technology-Center/Hour-Manager.git
  mv Hour-Manager/ hour_manager/
else
  cd hour_manager/
  echo "Checking Hour Manager"
  update-repo
  cd ..
fi

if [ ! -d lfp_scheduler/ ]
then
  echo "Cloning LFP Scheduler"
  git clone https://github.com/Student-Technology-Center/lfp_scheduler.git
else
  cd lfp_scheduler/
  echo "Checking LFP Scheduler"
  update-repo
  cd ..
fi

echo "Checking main project"
update-repo

if $restartServer
then
  tmux send-keys -t stc:2 C-c && (
    echo "Tmux wasn't found, this is no problemo"
  ) || (
    echo "Sending the restart command to the dev django server"
  )
fi
  