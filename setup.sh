#!/bin/bash
# Simply clones git repos

git clone https://github.com/Student-Technology-Center/django-wiki.git django-wiki
git clone https://github.com/Student-Technology-Center/Hour-Manager.git hour_manager
git clone https://github.com/Student-Technology-Center/evaluations.git evaluations
git clone https://github.com/Student-Technology-Center/lfp_scheduler.git lfp_scheduler

python3 manage.py makemigrations
python3 manage.py migrate
echo 'yes' | python3 manage.py collectstatic

