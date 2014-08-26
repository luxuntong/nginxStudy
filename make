#!/bin/sh
rm /tmp/echoLog
make
make install
killall -9 nginx;/usr/local/nginx/sbin/nginx
cat /tmp/echoLog
