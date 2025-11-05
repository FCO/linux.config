#!/bin/bash

for pad in $(swaymsg -t get_tree | jq -r '.nodes[].nodes[].floating_nodes[].marks|add' | grep 'scratch-')
do
    [ $pad == $1 ] || swaymsg move to scratchpad
done

swaymsg [con_mark="$1"] scratchpad show
swaymsg mode default
