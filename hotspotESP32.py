import network
import machine , time

wifi = network.WLAN(network.AP_IF)

wifi.active(True)

try:
    #networks = wifi.scan()
    #print(networks)
    
    wifi.config(essid = "Viveka",password = 'Viveka56301@',authmode=network.AUTH_WPA_WPA2_PSK)
    print(wifi.ifconfig())
except Exception as e:
    print(e)
except KeyboardInterrupt:
    print("EXIT")
    
