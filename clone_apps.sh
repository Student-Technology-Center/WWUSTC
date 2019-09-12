#!/bin/bash

branch=$1

# Default to master if no arg is given
if [[ -z "$1" ]]; then
    branch="master"
fi

while read line; do
    rm -r $line
    git clone "git@github.com:Student-Technology-Center/$line" \
        -b $branch
done < apps.txt
