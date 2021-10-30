#!/bin/sh

cal -n 3

read -p "" -n 1 -r
if [[ $REPLY =~ ^[Qq]$ ]]
then
	exit
fi
