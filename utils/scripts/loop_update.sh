#!/bin/bash
sleepTime=$2
prod=$1
while true; do ./update.sh $1; sleep $2; done;
