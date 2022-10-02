#! /bin/bash
sudo apt install jq
sudo apt install curl
#miniz
mkdir "$(pwd)/miners/miniz"
miniz=$(curl https://api.github.com/repos/miniZ-miner/miniZ/releases/latest| jq -r ".assets[] | select(.name | test(\"tar.gz\")) | .browser_download_url")
wget $miniz
tar -xf miniZ* --dir="$(pwd)/miners/miniz"
rm miniZ*

#lolminer
mkdir "$(pwd)/miners/lolminer"
lolminer=$(curl https://api.github.com/repos/Lolliedieb/lolMiner-releases/releases/latest| jq -r ".assets[] | select(.name | test(\"_Lin64.tar.gz\")) | .browser_download_url")
wget $lolminer
tar -xf lolMiner* --dir="$(pwd)/miners/lolminer" --strip-components=1
rm lolMiner*

#trex
mkdir "$(pwd)/miners/trex"
trex=$(curl https://api.github.com/repos/trexminer/T-Rex/releases/latest| jq -r ".assets[] | select(.name | test(\"tar.gz\")) | .browser_download_url")
wget $trex
tar -xf t-rex* --dir="$(pwd)/miners/trex"
rm t-rex*

#teamredminer
mkdir "$(pwd)/miners/teamredminer"
trm=$(curl https://api.github.com/repos/todxx/teamredminer/releases/latest| jq -r ".assets[] | select(.name | test(\"linux.tgz\")) | .browser_download_url")
wget $trm
tar -xf teamredminer* --dir="$(pwd)/miners/teamredminer" --strip-components=1
rm teamredminer*
