#!/bin/bash

REPOSITORY="https://github.com/Retroflux/playground/"

apt update
apt upgrade -y
apt install git -y
apt install make -y
apt install gcc -y
mkdir serverCode
git clone $REPOSITORY ./serverCode
make -C serverCode/GooglePresentationCode &> makeOutput.txt
chmod u+x serverCode
reboot
