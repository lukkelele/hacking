#!/bin/bash

URL=$1
echo "
________________________________________________
| Search website for a particular expression.  |
| by Lukkelele                                 |
|______________________________________________|

Website:
===> $URL"
mkdir ./webpage
cd ./webpage
wget -mq $1

ANSWER=$(grep -R $2)
cd ..
rm -r webpage
echo "
MATCH FOUND!
===> $ANSWER
"
