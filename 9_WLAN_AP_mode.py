# MicroPython Script for ESP32
# Author: Viveka Kushwaha

# ESP32 Wi-Fi Access Point Mode

import network
import machine , time

# object for wlan
wifi = network.WLAN(network.AP_IF)

# activate wifi driver
wifi.active(True)

try:
    #networks = wifi.scan()
    #print(networks)
    
    # wifi configuration for esp32
    wifi.config(essid = "Viveka",password = 'Viveka56301@',authmode=network.AUTH_WPA_WPA2_PSK)
    print(wifi.ifconfig())
except Exception as e:
    print(e)
except KeyboardInterrupt:
    print("EXIT")
    
