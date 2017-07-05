#!/bin/bash
update=false

apps=(
  hour_manager 
  lfp_scheduler 
)

## The cas check is temporary code, if CAS is to be removed, this check will be removed.
## If cas was to be used, we would need to implement CAS as a git submodule
if [ ! -d cas/ ]
then
  echo "Cloning Django-Cas"
  git clone https://github.com/kstateome/django-cas.git
  mv django-cas/cas/ cas/
  rm -rf django-cas/
fi

check-repo ()
{
  git remote update
  
  UPSTREAM=${1:-'@{u}'}
  LOCAL=$(git rev-parse @)
  REMOTE=$(git rev-parse "$UPSTREAM")
  BASE=$(git merge-base @ "$UPSTREAM")

  if [ $LOCAL = $REMOTE ]; then
      echo "Up-to-date"
  elif [ $LOCAL = $BASE ]; then
      echo "Update found, staging to update"
      if $1
      then
        git pull
      else
        update=true
      fi
  elif [ $REMOTE = $BASE ]; then
      echo "Local files have been edited."
  else
      echo "Diverged"
  fi
}



for item in ${apps[*]}
do
  printf "Cheking %s\n" $item
  if [ "$(ls -A $item)" ]; then
    # Not Empty
    cd $item/
    check-repo
    cd ..
    
    if $update; then break; fi
  else
    # Empty Folder
    # If there's an empty folder, we initialize the submodules and update regardless of the state of the other items.
    git submodule init
    git submodule update
    exit 
  fi
done

# Checks the main directory
check-repo true

if $update
then
  echo "Updating Repos"
  git submodule update
  
  echo "Attempting to send tmux command"
  tmux send-keys -t stc:2 C-c && (
    echo "Succesfully told django to restart"
  ) || (
    echo "Tmux wasn't found, this is no problemo"
  )
fi