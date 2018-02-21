#!/bin/bash

# Avalon7
if [ "$1" == "avalon7" ] && [ "$2" == "rpi1" ]; then
    [ -d ./avalon ] && rm ./avalon/*
    wget -P ./avalon https://canaan.io/downloads/software/avalon741/openwrt/latest/rpi1-modelb/openwrt-brcm2708-bcm2708-rpi-ext4-sdcard.img.gz
elif [ "$1" == "avalon7" ] && [ "$2" == "rpi2" ]; then
    [ -d ./avalon ] && rm ./avalon/*
    wget -P ./avalon https://canaan.io/downloads/software/avalon741/openwrt/latest/rpi2-modelb/openwrt-brcm2708-bcm2709-rpi-2-ext4-sdcard.img.gz
elif [ "$1" == "avalon7" ] && [ "$2" == "rpi3" ]; then
    [ -d ./avalon ] && rm ./avalon/*
    wget -P ./avalon https://canaan.io/downloads/software/avalon741/openwrt/latest/rpi3-modelb/openwrt-brcm2708-bcm2710-rpi-3-ext4-sdcard.img.gz

# Avalon6
elif [ "$1" == "avalon6" ] && [ "$2" == "rpi1" ]; then
    [ -d ./avalon ] && rm ./avalon/*
    wget -P ./avalon https://canaan.io/downloads/software/avalon6/openwrt/latest/brcm2708/bcm2708/openwrt-brcm2708-bcm2708-rpi-ext4-sdcard.img.gz
elif [ "$1" == "avalon6" ] && [ "$2" == "rpi2" ]; then
    [ -d ./avalon ] && rm ./avalon/*
    wget -P ./avalon https://canaan.io/downloads/software/avalon6/openwrt/latest/brcm2708/bcm2709/openwrt-brcm2708-bcm2709-rpi-2-ext4-sdcard.img.gz
elif [ "$1" == "avalon6" ] && [ "$2" == "rpi3" ]; then
    [ -d ./avalon ] && rm ./avalon/*
    wget -P ./avalon https://canaan.io/downloads/software/avalon6/openwrt/latest/brcm2708/bcm2710/openwrt-brcm2708-bcm2710-rpi-3-ext4-sdcard.img.gz

# Avalon8
elif [ "$1" == "avalon8" ] && [ "$2" == "rpi3" ]; then
    [ -d ./avalon ] && rm ./avalon/*
    wget -P ./avalon https://canaan.io/downloads/software/avalon821/openwrt/latest/rpi3-modelb/openwrt-brcm2708-bcm2710-rpi-3-ext4-sdcard.img.gz

fi
