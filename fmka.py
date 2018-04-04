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

conf_file = "openwrt.conf"

def mount_img():
    logging.debug("mount img file")

    subprocess.call("mkdir mount", shell=True)
    #subprocess.call("gzip -d openwrt-brcm2708-bcm2710-rpi-3-ext4-sdcard.img.gz", shell=True)
    subprocess.call("sudo mount -t auto -o loop,offset=$((57344*512)) ./openwrt-brcm2708-bcm2710-rpi-3-ext4-sdcard.img ./mount", shell=True)

def network_config():
    logging.debug("network config")

    with open(conf_file) as conf:
        for net in conf.readlines():
            if (net.find('ipaddr') != -1) or (net.find('gateway') != -1) or (net.find('dns') != -1) or (net.find('broadcast') != -1):
                if (net[0] == '#'):
                    continue
                tmp = net.strip()
                print(tmp)
            elif (net.find('dhcp') != -1):
                if (net[0] == '#'):
                    continue
                tmp = net.strip()
                break

    '''
    if (tmp[0] == "protocol"):
        if (tmp[1] == "dhcp"):
            subprocess.call("sudo sed -i '6,$ s/static/dhcp/g' ./mount/etc/config/network", shell=True)
            subprocess.call("sudo sed -i "/'netmask' '255.255.255.0'/d" ./mount/etc/config/network", shell=True)
            subprocess.call("sudo sed -i "/'ipaddr' '192.168.0.100'/d" ./mount/etc/config/network", shell=True)
            subprocess.call("sudo sed -i '/gateway/d' ./mount/etc/config/network", shell=True)
            subprocess.call("sudo sed -i '/dns/d' ./mount/etc/config/network", shell=True)
            subprocess.call("sudo sed -i '/broadcast/d' ./mount/etc/config/network", shell=True)
    else:
        if (tmp[0] == "ipaddr"):
            subprocess.call("sudo sed -i "s/option 'ipaddr' '192.168.0.100'/option 'ipaddr' 'tmp[1]'/g" ./mount/etc/config/network", shell=True)
        elif (tmp[0] == "gateway"):
            subprocess.call("sudo sed -i "s/option 'gateway' '192.168.0.1'/option 'gateway' 'tmp[1]'/g" ./mount/etc/config/network", shell=True)
        elif (tmp[0] == "dns"):
            subprocess.call("sudo sed -i "s/option dns '192.168.0.1'/option dns 'tmp[1]'/g" ./mount/etc/config/network", shell=True)
        elif (tmp[0] == "broadcast"):
            subprocess.call("sudo sed -i "s/option broadcast '192.168.0.255'/option broadcast '$2'/g" ./mount/etc/config/network", shell=True)
        else:
            logging.debug("parameter error.")
    '''

def timezone_config():
    logging.debug("timezone config")

def ntp_config():
    logging.debug("ntp config")

def pools_config():
    logging.debug("pools config")

def umount_img():
    logging.debug("umount img file")
    subprocess.call("sudo umount ./mount", shell=True)
    subprocess.call("rm -fr ./mount", shell=True)

if __name__ == '__main__':
    mount_img()
    network_config()
    umount_img()
