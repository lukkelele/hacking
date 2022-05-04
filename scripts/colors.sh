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

printf "I am ${RED}Lukas${NC}\n"


while getopts "color:s:" opt
do
  case "$opt" in
    color) c="$OPTARG" ;;
    s) str="$OPTARG" ;;
  esac
done

echo "$c"

