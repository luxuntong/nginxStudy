#!/bin/sh
make
make install
killall -9 nginx;/usr/local/nginx/sbin/nginx