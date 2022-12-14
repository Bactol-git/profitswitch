#! /bin/bash
systemctl --user stop profitswitch.service

sudo rm /etc/systemd/user/profitswitch.service
systemctl --user daemon-reload

sudo rm /etc/sudoers.d/profitswitch_include_file

FILE=/etc/sudoers.d/profitswitch_include_file
if test -f "$FILE"; then
    echo "Something went wrong"
fi
