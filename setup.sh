#! /bin/bash
sed "s@replacethis@$(pwd)@" profitswitch_startup.service.temp > profitswitch_startup.service
sed "s@replacethis@$(pwd)/profitswitch.py@" profitswitch.service.temp > profitswitch.service_temp_del
sed "s@replacedir@$(pwd)@" profitswitch.service_temp_del > profitswitch.service


rm profitswitch.service_temp_del
sudo mv profitswitch_startup.service /etc/systemd/user
FILE=/etc/systemd/user/profitswitch_startup.service
if test -f "$FILE"; then
    echo "Startup service created"
fi
sudo mv profitswitch.service /etc/systemd/user
FILE=/etc/systemd/user/profitswitch.service
if test -f "$FILE"; then
    echo "Switching service created"
fi

sudo systemctl daemon-reload

systemctl --user enable profitswitch_startup.service
systemctl --user enable profitswitch.service

user=$(who -q| sed -n 1p | cut -f 1 -d " ")
add_permission_eth='"ALL=(ALL) NOPASSWD: $(pwd)/profitswitch_eth"'
add_permission_flux='"ALL=(ALL) NOPASSWD: $(pwd)/profitswitch_flux"'
add_permission_erg='"ALL=(ALL) NOPASSWD: $(pwd)/profitswitch_erg"'
add_permission_etc='"ALL=(ALL) NOPASSWD: $(pwd)/profitswitch_etc"'
add_permission_kill='"ALL=(ALL) NOPASSWD: /bin/kill"'

sudo bash -c "echo $user $add_permission_eth >> /etc/sudoers.d/profitswitch_include_file"
sudo bash -c "echo $user $add_permission_flux >> /etc/sudoers.d/profitswitch_include_file"
sudo bash -c "echo $user $add_permission_erg >> /etc/sudoers.d/profitswitch_include_file"
sudo bash -c "echo $user $add_permission_etc >> /etc/sudoers.d/profitswitch_include_file"
sudo bash -c "echo $user $add_permission_kill >> /etc/sudoers.d/profitswitch_include_file"

chmod +x -R *

FILE=/etc/sudoers.d/profitswitch_include_file
if test -f "$FILE"; then
    echo "Sudoers file created: Setup finished"
fi

