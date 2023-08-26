import machine,neopixel
import time

pix = 1
led_pin = 48

np = neopixel.NeoPixel(machine.Pin(led_pin), pix)

while True:
    np[0] = (255, 0, 0)  # Set color to red (RGB: 255, 0, 0)
    np.write()
    time.sleep(0.5)

    np[0] = (0, 255, 0)  # Set color to green (RGB: 0, 255, 0)
    np.write()
    time.sleep(0.4)

    np[0] = (0, 0, 255)  # Set color to blue (RGB: 0, 0, 255)
    np.write()
    time.sleep(0.5)
    np[0] = (255,255,0)
    np.write()
    time.sleep(0.4)
    np[0] = (41,246,246)
    np.write()
    time.sleep(0.5)
    
    np[0] = (1,16,16)
    np.write()
    time.sleep(0.4)
    
    np[0] = (194,209,63)
    np.write()
    time.sleep(0.4)
    
    np[0] = (233,243,139)
    np.write()
    time.sleep(0.4)

