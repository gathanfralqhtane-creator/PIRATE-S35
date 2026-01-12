#!/bin/bash
clear
echo -e "\e[1;31m"
figlet "PIRATE-S35"
echo -e "\e[1;33m[*] جاري تثبيت ترسانة PIRATE-S35... الرجاء الانتظار.\e[0m"
pkg update && pkg upgrade -y
pkg install python nmap aircrack-ng figlet ruby curl -y
gem install lolcat
chmod +x pirate.py
echo -e "\e[1;32m[+] اكتمل التثبيت بنجاح يا بطل!\e[0m"
