import sys
import os

if __name__ == '__main__':
    '''
    check if user has su rights!
    If not root of sudo command used then exit script!
    '''
    if os.getuid() != 0:
        sys.exit('You must run this script as root or with sudo command!')
    if (len(sys.argv)!=3):
        print ('Usage: sudo python wpachange.py SSID WIFIPASSWORD')
        print ("Please add ssid and password to write to wpa_supplicant.conf file!")
        print ("Wifi credentials now are:\n")
        sys.exit((open("/etc/wpa_supplicant/wpa_supplicant.conf", "r")).read())
    ssid = sys.argv[1]
    wifipass = sys.argv[2]
    quotes = '"'
    line0 = "ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev\n"
    line1 = "update_config=1\ncountry=BE\n\n"
    line2 = 'network={\n\tssid=' + quotes + ssid + quotes
    line3 = '\n\tpsk=' + quotes + wifipass + quotes
    with open("/etc/wpa_supplicant/wpa_supplicant.conf", "w") as f:
        f.write(line0 + line1 + line2 + line3 + "\n}")
    f.close()
    sys.exit(f'wpa_supplicant.conf written with the new credentials\nSSID:{ssid}\nPassword:{wifipass}')
