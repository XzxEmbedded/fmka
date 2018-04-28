#!/bin/bash
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

[ -z "$PASSWORD" ] && PASSWORD="123"

mount_img() {
    echo "mount img file"
    
    if [ ! -d ./img/mount ]; then
        mkdir -p ./img/mount
    else
        rm -f ./img/openwrt*
    fi
    
    if [ "$1" == "controller_type" ]; then
        if [ "$2" == "rpi1" ]; then
            cp ./avalon/openwrt-brcm2708-bcm2708-rpi-ext4-sdcard.img.gz ./img/
            gzip -d ./img/openwrt-brcm2708-bcm2708-rpi-ext4-sdcard.img.gz 
            sudo mount -t auto -o loop,offset=$((57344*512)) ./img/openwrt-brcm2708-bcm2708-rpi-ext4-sdcard.img ./img/mount
        elif [ "$2" == "rpi2" ]; then
            cp ./avalon/openwrt-brcm2708-bcm2709-rpi-2-ext4-sdcard.img.gz ./img/
            gzip -d ./img/openwrt-brcm2708-bcm2709-rpi-2-ext4-sdcard.img.gz
            sudo mount -t auto -o loop,offset=$((57344*512)) ./img/openwrt-brcm2708-bcm2709-rpi-2-ext4-sdcard.img ./img/mount
        elif [ "$2" == "rpi3" ]; then
            cp ./avalon/openwrt-brcm2708-bcm2710-rpi-3-ext4-sdcard.img.gz ./img/
            gzip -d ./img/openwrt-brcm2708-bcm2710-rpi-3-ext4-sdcard.img.gz
            echo "$PASSWORD" | sudo -S mount -t auto -o loop,offset=$((57344*512)) ./img/openwrt-brcm2708-bcm2710-rpi-3-ext4-sdcard.img ./img/mount
        fi
    fi
}

# Network config
network_config() {
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
}

# Tiemzone config
timezone_config() {
    cd ./img/mount/etc/config

    sudo sed -i 's/timezone/'$1'/g' ./system
    sudo sed -i 's?UTC?'$2'?g' ./system
}

# Ntp server config
ntp_config() {
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
}

# Pools config
pools_config() {
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
}

# Umount img file
umount_img() {
    echo "umount img file"
    sleep 3
    sudo umount ./img/mount
}

for i in "$1"
do
    case $i in
        --mount)
            mount_img $2 $3
            ;;
        --network)
            network_config $2 $3
            ;;
        --timezone)
            timezone_config $2 $3
            ;;
        --ntp)
            ntp_config $2 $3
            ;;
        --pools)
            pools_config $2 $3
            ;;
        --umount)
            umount_img
            ;;
    esac
done

# vim: set ts=4 sw=4 et
