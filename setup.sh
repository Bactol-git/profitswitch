#! /bin/bash
sudo apt install curl

chmod +x -R *
sed "s@replacethis@$(pwd)/profitswitch.py@" profitswitch.service.temp > profitswitch.service_temp_del
sed "s@replacedir@$(pwd)@" profitswitch.service_temp_del > profitswitch.service


rm profitswitch.service_temp_del

sudo mv profitswitch.service /etc/systemd/user
FILE=/etc/systemd/user/profitswitch.service
if test -f "$FILE"; then
    echo "Switching service created"
fi


sudo systemctl daemon-reload

systemctl --user enable profitswitch.service

user=$(who -q| sed -n 1p | cut -f 1 -d " ")
add_permission_zil='"ALL=(ALL) NOPASSWD: $(pwd)/zilswitch_zil"'
add_permission_cfx='"ALL=(ALL) NOPASSWD: $(pwd)/profitswitch_cfx"'
add_permission_erg='"ALL=(ALL) NOPASSWD: $(pwd)/profitswitch_erg"'
add_permission_etc='"ALL=(ALL) NOPASSWD: $(pwd)/profitswitch_etc"'
add_permission_flux='"ALL=(ALL) NOPASSWD: $(pwd)/profitswitch_flux"'
add_permission_rvn='"ALL=(ALL) NOPASSWD: $(pwd)/profitswitch_rvn"'
add_permission_firo='"ALL=(ALL) NOPASSWD: $(pwd)/profitswitch_firo"'
add_permission_ethw='"ALL=(ALL) NOPASSWD: $(pwd)/profitswitch_ethw"'
add_permission_beam='"ALL=(ALL) NOPASSWD: $(pwd)/profitswitch_beam"'


add_permission_amd_OC_cfx='"ALL=(ALL) NOPASSWD: $(pwd)/overclocks/amd_OC_cfx"'
add_permission_nvidia_OC_cfx='"ALL=(ALL) NOPASSWD: $(pwd)/overclocks/nvidia_OC_cfx"'
add_permission_amd_OC_erg='"ALL=(ALL) NOPASSWD: $(pwd)/overclocks/amd_OC_erg"'
add_permission_nvidia_OC_erg='"ALL=(ALL) NOPASSWD: $(pwd)/overclocks/nvidia_OC_erg"'
add_permission_amd_OC_etc='"ALL=(ALL) NOPASSWD: $(pwd)/overclocks/amd_OC_etc"'
add_permission_nvidia_OC_etc='"ALL=(ALL) NOPASSWD: $(pwd)/overclocks/nvidia_OC_etc"'
add_permission_amd_OC_flux='"ALL=(ALL) NOPASSWD: $(pwd)/overclocks/amd_OC_flux"'
add_permission_nvidia_OC_flux='"ALL=(ALL) NOPASSWD: $(pwd)/overclocks/nvidia_OC_flux"'
add_permission_amd_OC_rvn='"ALL=(ALL) NOPASSWD: $(pwd)/overclocks/amd_OC_rvn"'
add_permission_nvidia_OC_rvn='"ALL=(ALL) NOPASSWD: $(pwd)/overclocks/nvidia_OC_rvn"'
add_permission_amd_OC_firo='"ALL=(ALL) NOPASSWD: $(pwd)/overclocks/amd_OC_firo"'
add_permission_nvidia_OC_firo='"ALL=(ALL) NOPASSWD: $(pwd)/overclocks/nvidia_OC_firo"'
add_permission_amd_OC_ethw='"ALL=(ALL) NOPASSWD: $(pwd)/overclocks/amd_OC_ethw"'
add_permission_nvidia_OC_ethw='"ALL=(ALL) NOPASSWD: $(pwd)/overclocks/nvidia_OC_ethw"'
add_permission_amd_OC_beam='"ALL=(ALL) NOPASSWD: $(pwd)/overclocks/amd_OC_beam"'
add_permission_nvidia_OC_beam='"ALL=(ALL) NOPASSWD: $(pwd)/overclocks/nvidia_OC_beam"'

add_permission_kill='"ALL=(ALL) NOPASSWD: /bin/kill"'
add_permission_pkill='"ALL=(ALL) NOPASSWD: /bin/pkill"'

sudo bash -c "echo $user $add_permission_zil >> /etc/sudoers.d/profitswitch_include_file"
sudo bash -c "echo $user $add_permission_cfx >> /etc/sudoers.d/profitswitch_include_file"
sudo bash -c "echo $user $add_permission_erg >> /etc/sudoers.d/profitswitch_include_file"
sudo bash -c "echo $user $add_permission_etc >> /etc/sudoers.d/profitswitch_include_file"
sudo bash -c "echo $user $add_permission_flux >> /etc/sudoers.d/profitswitch_include_file"
sudo bash -c "echo $user $add_permission_rvn >> /etc/sudoers.d/profitswitch_include_file"
sudo bash -c "echo $user $add_permission_firo >> /etc/sudoers.d/profitswitch_include_file"
sudo bash -c "echo $user $add_permission_ethw >> /etc/sudoers.d/profitswitch_include_file"
sudo bash -c "echo $user $add_permission_beam >> /etc/sudoers.d/profitswitch_include_file"

sudo bash -c "echo $user $add_permission_amd_OC_cfx >> /etc/sudoers.d/profitswitch_include_file"
sudo bash -c "echo $user $add_permission_nvidia_OC_cfx >> /etc/sudoers.d/profitswitch_include_file"
sudo bash -c "echo $user $add_permission_amd_OC_erg >> /etc/sudoers.d/profitswitch_include_file"
sudo bash -c "echo $user $add_permission_nvidia_OC_erg >> /etc/sudoers.d/profitswitch_include_file"
sudo bash -c "echo $user $add_permission_amd_OC_etc >> /etc/sudoers.d/profitswitch_include_file"
sudo bash -c "echo $user $add_permission_nvidia_OC_etc >> /etc/sudoers.d/profitswitch_include_file"
sudo bash -c "echo $user $add_permission_amd_OC_flux >> /etc/sudoers.d/profitswitch_include_file"
sudo bash -c "echo $user $add_permission_nvidia_OC_flux >> /etc/sudoers.d/profitswitch_include_file"
sudo bash -c "echo $user $add_permission_amd_OC_rvn >> /etc/sudoers.d/profitswitch_include_file"
sudo bash -c "echo $user $add_permission_nvidia_OC_rvn >> /etc/sudoers.d/profitswitch_include_file"
sudo bash -c "echo $user $add_permission_amd_OC_firo >> /etc/sudoers.d/profitswitch_include_file"
sudo bash -c "echo $user $add_permission_nvidia_OC_firo >> /etc/sudoers.d/profitswitch_include_file"
sudo bash -c "echo $user $add_permission_amd_OC_ethw >> /etc/sudoers.d/profitswitch_include_file"
sudo bash -c "echo $user $add_permission_nvidia_OC_ethw >> /etc/sudoers.d/profitswitch_include_file"
sudo bash -c "echo $user $add_permission_amd_OC_beam >> /etc/sudoers.d/profitswitch_include_file"
sudo bash -c "echo $user $add_permission_nvidia_OC_beam >> /etc/sudoers.d/profitswitch_include_file"

sudo bash -c "echo $user $add_permission_kill >> /etc/sudoers.d/profitswitch_include_file"
sudo bash -c "echo $user $add_permission_pkill >> /etc/sudoers.d/profitswitch_include_file"
