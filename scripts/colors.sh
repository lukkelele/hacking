#!/bin/bash

RED='\033[0;31m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
GREEN='\033[0;32m'
WHITE='\033[1;37m'
BROWN='\033[0;33m'
BLACK='\033[0;30m'
PURPLE='\033[0;35m'
YELLOW='\033[1;33m'
DARKGRAY='\033[1;30m'
LIGHTGRAY='\033[0;37m'
LIGHTCYAN='\033[1;36m'
LIGHTCYAN='\033[1;36m'
LIGHTCYAN='\033[1;30m'
LIGHTRED='\033[1;31m'
LIGHTGREEN='\033[1;32m'
NC='\033[0m'


function print_color () {
  case $1 in
    red) COLOR=$RED ;;
    blue) COLOR=$BLUE ;;
    green) COLOR=$GREEN ;;
    cyan) COLOR=$CYAN ;;
    white) COLOR=$WHITE ;;
    purple) COLOR=$WHITE ;;
    yellow) COLOR=$YELLOW ;;
    brown) COLOR=$BROWN ;;
    black) COLOR=$BLACK ;;
    darkgray) COLOR=$DARKGRAY ;;
    lightgray) COLOR=$LIGHTGRAY ;;
    lightgreen) COLOR=$LIGHTGREEN ;;
    lightcyan ) COLOR=$LIGHTCYAN ;;

  esac

  printf "==>${COLOR} $2 ${NC}\n"
}

function arrow () {
  case $3 in
    red) COLOR=$RED ;;
    blue) COLOR=$BLUE ;;
    green) COLOR=$GREEN ;;
    cyan) COLOR=$CYAN ;;
    white) COLOR=$WHITE ;;
    purple) COLOR=$WHITE ;;
    yellow) COLOR=$YELLOW ;;
    brown) COLOR=$BROWN ;;
    black) COLOR=$BLACK ;;
    darkgray) COLOR=$DARKGRAY ;;
    lightgray) COLOR=$LIGHTGRAY ;;
    lightgreen) COLOR=$LIGHTGREEN ;;
    lightcyan ) COLOR=$LIGHTCYAN ;;
  esac
  printf "${COLOR}==>${NC} $2 ${NC}"
}
arrow $1 $2 $3
#print_color $1 "$2"
echo ''
