#notify-send "shutdown?"
echo "reboot?"
read -p "" -n 1 -r
if [[ $REPLY =~ ^[Yy]$ ]]
then
	reboot
fi
