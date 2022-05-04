#!/bin/bash

RED='\033[0;31m'
CYAN='\033[0;36m'
GREEN='\033[0;32m'
WHITE='\033[1;37m'
BLACK='\033[0;30m'
PURPLE='\033[0;35m'
YELLOW='\033[1;33m'
LIGHTCYAN='\033[0;37m'
LIGHTCYAN='\033[1;30m'
LIGHTRED='\033[1;31m'
LIGHTGREEN='\033[1;32m'
NC='\033[0m'

if [ "$1" == "YELLOW" ]
then
  COLOR=$YELLOW
elif [ "$1" == "GREEN" ]
then
  COLOR=$GREEN
elif [ "$1" == "BLACK" ]
then
  COLOR=$BLACK
elif [ "$1" == "WHITE" ]
then
  COLOR=$WHITE
elif [ "$1" == "CYAN" ]
then
  COLOR=$CYAN
elif [ "$1" == "PURPLE" ]
then
  COLOR=$PURPLE
elif [ "$1" == "RED" ]
then
  COLOR=$RED
fi

printf "==>${COLOR} $2 ${NC}\n"

