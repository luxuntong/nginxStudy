#!/bin/sh
rm /tmp/echoLog
./configure
make
make install
killall -9 nginx;/usr/local/nginx/sbin/nginx
