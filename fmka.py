#!/usr/bin/env python
# Tool's name is Firmware Modify Kit for Avalon(FMKA)
#
# October 2017 Zhenxing Xu <xuzhenxing@canaan-creative.com>

import os
import time

config_file = "openwrt.conf"

'''
def network_cmd(net):
    cmd = "./config_image.sh --network %s" %(net)
    os.system(cmd)

def ntp_cmd(ntp):
    cmd = "./config_image.sh --ntp %s" %(ntp)
    os.system(cmd)

def pool_cmd(pool):
    cmd = "./config_image.sh --pools %s" %(pool)
    os.system(cmd)
'''

# Mount img file
def mount_img():


'''
# Network
def network():
    conf = open("default.conf")
    for net in conf.readlines():
        if (net.find('ipaddr') != -1) or (net.find('gateway') != -1) or \
        (net.find('dns') != -1) or (net.find('broadcast') != -1):
            if (net[0] == '#'):
                continue
            network_cmd(net.strip())
        elif (net.find('dhcp') != -1):
            if (net[0] == '#'):
                continue
            network_cmd(net.strip())
            break
    conf.close()

# Timezone
def timezone():
    conf = open("default.conf")
    for time in conf.readlines():
        if (time.find('zonename') != -1):
            if (time[0] == '#'):
                continue
            cmd = "./config_image.sh --timezone %s" %(time.strip())
            os.system(cmd)
            break
    conf.close()

# Ntp server
def ntp_server():
    conf = open("default.conf")
    for ntp in conf.readlines():
        if (ntp.find('ntp_server') != -1) or (ntp.find('candidates1') != -1) or \
        (ntp.find('candidates1') != -1) or (ntp.find('candidates2') != -1) or \
        (ntp.find('candidates3') != -1) or (ntp.find('candidates4') != -1):
            if (ntp[0] == '#'):
                continue
            ntp_cmd(ntp.strip())
    conf.close()

# Pools Workers
def pools():
    conf = open("default.conf")
    for pool in conf.readlines():
        if (pool.find('pool1url') != -1) or (pool.find('pool1user') != -1) or (pool.find('pool1pw') != -1) or \
        (pool.find('pool2url') != -1) or (pool.find('pool2user') != -1) or (pool.find('pool2pw') != -1) or \
        (pool.find('pool3url') != -1) or (pool.find('pool3user') != -1) or (pool.find('pool3pw') != -1):
            if (pool[0] == '#'):
                continue
            pool_cmd(pool.strip())
    conf.close()
'''

# Umount img file
def umount_img():
    os.system("./config_image.sh --umount")

if __name__ == "__main__":
    mount_img()
    '''
    network()
    timezone()
    ntp_server()
    pools()
    '''
    umount_img()
    print("firmwae config success.")
