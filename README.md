# profitswitch

This is a program intended to help automate the process of chasing the most profitable coin for your rig. Only tested on 30-series nvidia and 6000-series amd. It should only affect overclock settings, so make sure the overclock settings are suppored for your cards.
Supported coins: ETH, FLUX, ERG, ETC, RVN, FIRO. More to come at some point.
1. git clone https://github.com/Bactol-git/profitswitch
2. cd profitswitch/
3. ./setup.sh
4. Make sure to set your own overclocks in the overclocking files in the overclocks directory.
5. Place your miners of choice in the miners directory. It is important to place them in this directory so that the program can close the previous miner when it switches. The script "setup_miners.sh" fetches the latest releases of lolminer, t-rex miner and miniZ and put them in the correct structure. If you use other miners, just put them in the miners folder and update the profitswitch_* files accordingly.
6. Configure the "profitswitch_*" scripts in the main directory to your own wallets, pools, miners and the directory of the miners. You can use the included as templates or to get a grasp of how it should be set up.
7. Set your rigs hash rate, power draw and your power rate (dollar/kWh) in the config file. You could also set the flux PA multiplier depending on your pools fee rate.
8. Set the "cards" entry in the config file to match your setup. The supported entries are: "amd", "nvidia" and "mixed". 
9. Manually check that the script functions as intended by running "python3 profitswitch_startup.py" from the main directory. If there is an error in the overclock file for the chosen mining algo the script will stop.

Now everything should be set. You will have to start the services in order for the mining scripts and switching to start. This can be done by running "systemctl --user start profitswitch.service".
These services will automatically start on reboots once they are set up, so you could also just do a reboot instead of running the command. Note also that the miner will start after 60 seconds on boot. This is in order to let all dependencies start up and to let you have time to stop the service before it starts up if that is ever needed. You could adjust this time in the "profitswitch_startup.service" service found in /etc/systemd/user.

The program is set up to check profitability every hour. This can be adjusted in the service "profitswitch.service", also found in /etc/systemd/user.

IMPORTANT for maintenance and possible issues: In order to stop the miner before it starts on boot you have to stop the profitswitch_startup.service before it goes off. You can do that by "systemctl --user stop profitswitch_startup.service". If it goes off you have to kill the miner process. You can find the PID by running "ps -ef | grep miners | grep -v grep | awk '{print $2}'". To kill it simply "kill number". Mark that this will not stop the hourly switching, so you would have to stop that aswell in order to completely stop the program "sudo systemctl --user stop profitswitch.service". The python script "killswitch.py" will kill both services and any running miners started by the program.

There is a python script called "check_profitability" that the program doesnt use, but is included so that you as a user can manually check your rigs projected profit (dollar a day) on the different algos. To run that simply run "python3 check_profitability" from the main directory.

Note that I can not guarantee that the API will stay up at all times, as these are external. If you want to use other APIs, feel free to modify the python scripts "profitswitch.py" and "profitswitch_startup.py".

There is a "uninstall_services.sh" script that will remove the systemd services and the sudoers file. The actual folder you placed and all the content will for the time being have to be removed manually. Make sure you dont delete the overclocks before you have moved them if you need them later.

If you decide to mine to unmineable please use the referral code: wuqt-715z. You will save a little on the pool fees, and I will get a small kickback.

Please feel free to donate some hash so I can keep coffee in my mug. Enjoy.
