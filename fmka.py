#!/usr/bin/env python3
#
# This is a script for creating user custom config img file
#
# October 2017 Zhenxing Xu <xuzhenxing@canaan-creative.com>
#
# Learn bash: http://explainshell.com/

# Mount img file
# Check offset value: fdisk -lu img.file
# eg. fdisk -lu openwrt-brcm2708-bcm2710-rpi-3-ext4-sdcard.img
# Output:
# Disk openwrt-brcm2708-bcm2710-rpi-3-ext4-sdcard.img: 79 MB, 79691776 bytes
# 255 heads, 63 sectors/track, 9 cylinders, total 155648 sectors
# Units = sectors of 1 * 512 = 512 bytes
# Sector size (logical/physical): 512 bytes / 512 bytes
# I/O size (minimum/optimal): 512 bytes / 512 bytes
# Disk identifier: 0x5452574f
#
#                                         Device Boot      Start         End      Blocks   Id  System
# openwrt-brcm2708-bcm2710-rpi-3-ext4-sdcard.img1   *        8192       49151       20480    c  W95 FAT32 (LBA)
# openwrt-brcm2708-bcm2710-rpi-3-ext4-sdcard.img2           57344      155647       49152   83  Lin

from __future__ import print_function
import subprocess
import logging

# Config logging level
logging.basicConfig(level=logging.DEBUG)

def mount_img():
    logging.debug("mount img file")

    subprocess.call("mkdir mount", shell=True)
    subprocess.call("gzip -d openwrt-brcm2708-bcm2710-rpi-3-ext4-sdcard.img.gz", shell=True)
    subprocess.call("sudo mount -t auto -o loop,offset=$((57344*512)) ./img/openwrt-brcm2708-bcm2710-rpi-3-ext4-sdcard.img ./mount", shell=True)

def network_config():
    logging.debug("network config")

    '''
    cd ./img/mount/etc/config

    if [ "$1" == "protocol" ]; then
        if [ "$2" == "dhcp" ]; then
            sudo sed -i '6,$ s/static/dhcp/g' ./network
            sudo sed -i "/'netmask' '255.255.255.0'/d" ./network
            sudo sed -i "/'ipaddr' '192.168.0.100'/d" ./network
            sudo sed -i '/gateway/d' ./network
            sudo sed -i '/dns/d' ./network
            sudo sed -i '/broadcast/d' ./network
        fi
    else
        if [ "$1" == "ipaddr" ]; then
            sudo sed -i "s/option 'ipaddr' '192.168.0.100'/option 'ipaddr' '$2'/g" ./network
        elif [ "$1" == "gateway" ]; then
            sudo sed -i "s/option 'gateway' '192.168.0.1'/option 'gateway' '$2'/g" ./network
        elif [ "$1" == "dns" ]; then
            sudo sed -i "s/option dns '192.168.0.1'/option dns '$2'/g" ./network
        elif [ "$1" == "broadcast" ]; then
            sudo sed -i "s/option broadcast '192.168.0.255'/option broadcast '$2'/g" ./network
        else
            echo "parameter error."
        fi
    fi
    '''

def timezone_config():
    logging.debug("timezone config")

    '''
    cd ./img/mount/etc/config

    sudo sed -i 's/timezone/'$1'/g' ./system
    sudo sed -i 's?UTC?'$2'?g' ./system
    '''

def ntp_config():
    logging.debug("ntp config")

    '''
    cd ./img/mount/etc/config

    if [ "$1" == "ntp_server" ]; then
        if [ "$2" == "enable" ]; then
            sudo sed -i "s/option enable_server 0/option enable_server '1'/g" ./system
        fi
    elif [ "$1" == "candidates1" ]; then
        sudo sed -i 's/0.openwrt.pool.ntp.org/'$2'/g' ./system
    elif [ "$1" == "candidates2" ]; then
        sudo sed -i 's/1.openwrt.pool.ntp.org/'$2'/g' ./system
    elif [ "$1" == "candidates3" ]; then
        sudo sed -i 's/2.openwrt.pool.ntp.org/'$2'/g' ./system
    elif [ "$1" == "candidates4" ]; then
        sudo sed -i 's/3.openwrt.pool.ntp.org/'$2'/g' ./system
    fi
    '''

def pools_config():
    logging.debug("pools config")

    '''
    cd ./img/mount/etc/config

    # Pool1
    if [ "$1" == "pool1url" ]; then
        sudo sed -i "s?'stratum+tcp://stratum.kano.is:3333'?'$2'?g" ./cgminer
    elif [ "$1" == "pool1user" ]; then
        sudo sed -i "s/'canaan.3333'/'$2'/g" ./cgminer
    elif [ "$1" == "pool1pw" ]; then
        sudo sed -i "s/option pool1pw          '1234'/option pool1pw          '$2'/g" ./cgminer
    fi

    # Pool2
    if [ "$1" == "pool2url" ]; then
        sudo sed -i "s?'stratum+tcp://stratum80.kano.is:80'?'$2'?g" ./cgminer
    elif [ "$1" == "pool2user" ]; then
        sudo sed -i "s/'canaan.80'/'$2'/g" ./cgminer
    elif [ "$1" == "pool2pw" ]; then
        sudo sed -i "s/option pool2pw          '1234'/option pool2pw          '$2'/g" ./cgminer
    fi

    # Pool3
    if [ "$1" == "pool3url" ]; then
        sudo sed -i "s?'stratum+tcp://stratum81.kano.is:81'?'$2'?g" ./cgminer
    elif [ "$1" == "pool3user" ]; then
        sudo sed -i "s/'canaan.81'/'$2'/g" ./cgminer
    elif [ "$1" == "pool3pw" ]; then
        sudo sed -i "s/option pool3pw          '1234'/option pool3pw          '$2'/g" ./cgminer
    fi
    '''

def umount_img():
    logging.debug("umount img file")
    subprocess.call("sudo umount ./mount", shell=True)
    subprocess.call("rm -fr ./mount")
