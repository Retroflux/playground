#!/bin/bash

REPOSITORY="https://github.com/Retroflux/playground/"

apt update
apt upgrade -y
apt install git -y
apt install make -y
apt install gcc -y
mkdir clientCode
git clone $REPOSITORY ./clientCode
make -C clientCode/GooglePresentationCode &> makeOutput.txt
chmod -R 755 /clientCode
reboot