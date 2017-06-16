#!/bin/bash

if [ ! -d cas/ ]
then
  echo "Cloning Django-Cas"
  git clone https://github.com/kstateome/django-cas.git
  mv django-cas/cas/ cas/
  rm -rf django-cas/
fi

if [ ! -d hour_manager/ ]
then
  echo "Cloning Hour Manager"
  git clone https://github.com/Student-Technology-Center/Hour-Manager.git
  mv Hour-Manager/ hour_manager/
else
  echo "Updating Hour-Manager..."
  cd hour_manager/
  git pull
  cd ..
fi

if [ ! -d lfp_scheduler/ ]
then
  echo "Cloning LFP Scheduler"
  git clone https://github.com/Student-Technology-Center/lfp_scheduler.git
else
  echo "Updating LFP Scheduler"
  cd lfp_scheduler/
  git pull
  cd ..
fi
