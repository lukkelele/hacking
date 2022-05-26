#!/bin/bash

# This is a better version of colors.sh 
# colors.sh will prob be removed later

RED="$(printf '\033[31m')"
GREEN="$(printf '\033[32m')"
ORANGE="$(printf '\033[33m')"
BLUE="$(printf '\033[34m')"
MAGENTA="$(printf '\033[35m')"
CYAN="$(printf '\033[36m')"
WHITE="$(printf '\033[37m')"
BLACK="$(printf '\033[30m')"
REDBG="$(printf '\033[41m')"
GREENBG="$(printf '\033[42m')"
ORANGEBG="$(printf '\033[43m')"
BLUEBG="$(printf '\033[44m')"
MAGENTABG="$(printf '\033[45m')"
CYANBG="$(printf '\033[46m')"
WHITEBG="$(printf '\033[47m')"
BLACKBG="$(printf '\033[40m')"
RESETBG="$(printf '\e[0m\n')"
NC="$(printf '\033[0m')"


banner_lukkelele() {
  cat <<- EOF
    ${ORANGE} _       _    _        _      _      
    ${ORANGE}| |_   _| | _| | _____| | ___| | ___  
    ${ORANGE}| | | | | |/ / |/ / _ \ |/ _ \ |/ _ \ 
    ${ORANGE}| | |_| |   <|   <  __/ |  __/ |  __/ 
    ${ORANGE}|_|\__,_|_|\_\_|\_\___|_|\___|_|\___| 
    ${NC}
EOF
}

banner_attepatte() {
  cat <<- EOF 
  ${GREEN}
  ${GREEN}   ____| |_| |_ ___ _ __   __ _| |_| |_ ___   
  ${GREEN}  / _  | __| __/ _ \ '  \ / _  | __| __| _ \  
  ${GREEN} | (_| | |_| ||  __/ |_) | (_| | |_| ||  __/   
  ${GREEN}  \__,_|\__|\__\___| .__/ \__,_|\__|\__\___|   
  ${GREEN}                   |_|                        
  ${NC}                                                 
EOF
}

banner_lukkelele
banner_attepatte
