#!/bin/bash
restartServer=false

update-repo ()
{
  git remote update
  
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

export -f update-repo

if [ ! -d cas/ ]
then
  echo "Cloning Django-Cas"
  runuser -l stc -c 'git clone https://github.com/kstateome/django-cas.git'
  mv django-cas/cas/ cas/
  rm -rf django-cas/
  restartServer=true
fi

if [ ! -d hour_manager/ ]
then
  echo "Cloning Hour Manager"
  runuser -l stc -c 'git clone https://github.com/Student-Technology-Center/Hour-Manager.git'
  mv Hour-Manager/ hour_manager/
else
  cd hour_manager/
  echo "Checking Hour Manager"
  runuser -l stc -c 'update-repo'
  cd ..
fi

if [ ! -d lfp_scheduler/ ]
then
  echo "Cloning LFP Scheduler"
  runuser -l stc -c 'git clone https://github.com/Student-Technology-Center/lfp_scheduler.git'
else
  cd lfp_scheduler/
  echo "Checking LFP Scheduler"
  runuser -l stc -c 'update-repo'
  cd ..
fi

echo "Checking main project"
runuser -l stc -c 'update-repo'

if $restartServer
then
  tmux send-keys -t stc:2 C-c && (
    echo "Tmux wasn't found, this is no problemo"
  ) || (
    echo "Sending the restart command to the dev django server"
  )
fi
  
