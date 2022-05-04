#!/bin/bash

echo "Running stack based overflow exploit using Perl"
bytesize=read()
nop_hex='0x90'
nop_sled=$bytesize*$nop_hex
echo "$bytesize"
