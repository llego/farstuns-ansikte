#!/bin/bash

wlr-randr --output DPI-1 --transform 90
export imv_config="/home/llego/farstuns-ansikte/imv_config"

sleep 5

echo "Refreshing screen"
/usr/bin/imv-wayland /home/llego/farstuns-ansikte/receive.jpg

