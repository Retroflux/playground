#!/bin/bash

REPOSITORY="https://github.com/Retroflux/playground/"

apt update
apt upgrade -y
apt install git -y
apt install apache2 -y
apt install make -y
apt install gcc -y
mkdir serverCode
git clone $REPOSITORY ./serverCode
systemctl start apache2
bash -c 'echo your very first web server > /var/www/html/index.html'
make -C serverCode/GooglePresentationCode &> makeOutput.txt
reboot
