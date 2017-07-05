#!/bin/bash

apps=(
  hour_manager 
  lfp_scheduler 
)

check-repo ()
{
  git remote update
  
  UPSTREAM=${1:-'@{u}'}
  LOCAL=$(git rev-parse @)
  REMOTE=$(git rev-parse "$UPSTREAM")
  BASE=$(git merge-base @ "$UPSTREAM")

  if [[ $LOCAL = $REMOTE ]]; then echo "Up-to-date";
  elif [[ $LOCAL = $BASE ]]; then 
    echo "Update found, staging to update"; 
    git pull;
    tmux send-keys -t stc:2 C-c && (
      echo "Succesfully told django to restart"
    ) || (
      echo "Tmux wasn't found, this is no problemo"
    )
  elif [[ $REMOTE = $BASE ]]; then echo "Local files have been edited.";
  else echo "Diverged";
  fi
}

## The cas check is temporary code, if CAS is to be removed, this check will be removed.
## If cas was to be used, we would need to implement CAS as a git submodule
if [ ! -d cas/ ]
then
  echo "Cloning Django-Cas"
  git clone https://github.com/kstateome/django-cas.git
  mv django-cas/cas/ cas/
  rm -rf django-cas/
fi

for item in ${apps[*]}
do
  printf "Cheking %s\n" $item
  if ! [[ "$(ls -A $item)" ]]; then
    git submodule init
  fi
done

echo "Updating Repos"
git submodule update
check-repo
