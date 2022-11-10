# profitswitch

This is a program intended to help automate the process of chasing the most profitable coin for your rig. Only tested on 30-series nvidia and 6000-series amd. It should only affect overclock settings, so make sure the overclock settings are suppored for your cards.
Supported coins: ETHW, FLUX, ERG, ETC, RVN, FIRO, ZIL, BEAM, KAS. More to come at some point.
1. git clone https://github.com/Bactol-git/profitswitch
2. cd profitswitch/
3. ./setup.sh
4. Make sure to set your own overclocks in the overclocking files in the overclocks directory.
5. Place your miners of choice in the miners directory. It is important to place them in this directory so that the program can close the previous miner when it switches. The script "setup_miners.sh" fetches the latest releases of lolminer, t-rex miner, teamredminer and miniZ and put them in the correct structure. If you use other miners, just put them in the miners folder and update the profitswitch_* files accordingly.
6. Configure the "profitswitch_*" scripts in the main directory to your own wallets, pools, miners and the directory of the miners. You can use the included as templates or to get a grasp of how it should be set up.
7. Set your rigs hash rate, power draw and your power rate (dollar/kWh) in the config file. You could also set the flux PA multiplier depending on your pools fee rate.
8. Set the "cards" entry in the config file to match your setup. The supported entries are: "amd", "nvidia" and "mixed". 
9. Manually check that the script functions as intended by running "python3 profitswitch_startup.py" from the main directory. If there is an error in the overclock file for the chosen mining algo the script will stop.

Now everything should be set. You will have to start the services in order for the mining scripts and switching to start. This can be done by running "systemctl --user start profitswitch.service".
These services will automatically start on reboots once they are set up, so you could also just do a reboot instead of running the command.

The program is set up to check profitability on startup, then switching to zil while their PoW block is active, and then checks profitability and switches again.

IMPORTANT for maintenance and possible issues: The python script "killswitch.py" will kill the profitswitch service and any running miners started by the program.

There is a python script called "check_profitability" that the program doesnt use, but is included so that you as a user can manually check your rigs projected profit (dollar a day) on the different algos. To run that simply run "python3 check_profitability" from the main directory.

If you want to see the miner running start the script "show_miner.sh". It will promt you for root password as the miners are ran as sudo to unlock LHR.

Note that I can not guarantee that the API will stay up at all times, as these are external. If you want to use other APIs, feel free to modify the python scripts "profitswitch.py" and "profitswitch_startup.py".

There is a "uninstall_services.sh" script that will remove the systemd services and the sudoers file. The actual folder you placed and all the content will for the time being have to be removed manually. Make sure you dont delete the overclocks before you have moved them if you need them later.

If you decide to mine to unmineable please use the referral code: wuqt-715z. You will save a little on the pool fees, and I will get a small kickback.

Please feel free to donate some hash so I can keep coffee in my mug. Enjoy.
