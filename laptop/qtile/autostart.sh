#!/bin/sh

nitrogen --restore &

picom --experimental-backends &

brightnessctl set 16%

xmodmap ~/.Xmodmap
