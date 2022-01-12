#!/bin/sh

nitrogen --restore &

imwheel -b 45

# natural scroll
#xinput set-button-map 8 1 2 3 5 4 6 7 8 9 10

# mouse speed
xinput set-prop 8 "libinput Accel Speed" -.47
