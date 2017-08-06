#!/bin/bash

# restart is a variable where if set to true, at the end of this script, the django server will restart 
restart=false

# List of apps are listed to iterate through, these are all the current submodules
apps=(
  hour_manager 
  django-wiki
	lfp_scheduler
)

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
    git pull;
    restart=true
  elif [[ $REMOTE = $BASE ]]; then echo "Local files have been edited.";
  else echo "Diverged";
  fi
  
  echo "-----------------------"
  echo ""
}

echo ""

# We start to iterate through the apps...
for item in ${apps[*]}
do
  # If any folder is empty, this is a sign of a fresh clone
  if ! [[ "$(ls -A $item)" ]]; then
    echo "Updating all submodules and checking branch master."
    echo "-----------------------"
    
    # Upon a fresh clone, we'll initialize all the submodules and update them
    git submodule init
    git submodule update
    
    # Afterwards, we'll iterate through all of them again and checkt them out to master branch
    # TODO: pass a variable to define branch as to not diverge prod from master
    for app in ${apps[*]}
    do
      echo "Checking out $app..."
      cd $app
      git checkout master
      git pull
      cd ..
    done
    # We break because this particular for loop is only for submodules and we've done what we can
    break
  fi
  
  # Otherwise, we'll simply enter the app's directory and perform the check-repo function
  echo "Updating $item..."
  cd $item
  check-repo
  cd ..
done

# Same thing as before, just with the main repo 
echo "Updating WWU STC Django Project..."
check-repo

# Sends the restart command to django if needed
if $restart; then
  tmux send-keys -t stc:2 C-c && (
    echo "Succesfully told django to restart"
  ) || (
    echo "Tmux wasn't found, this is no problemo"
  )
fi
