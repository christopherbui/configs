notify-send "shutdown?"
read -p "" -n 1 -r
if [[ $REPLY =~ ^[Yy]$ ]]
then
	shutdown now
fi
