#!/bin/bash

display=$1
wallpaper=$2

echo $wallpaper > /tmp/wallpaper.txt
hellwal -q -i "$wallpaper"
