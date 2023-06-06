import network
import socket
import time
import struct

import ssd1306
from machine import Pin, I2C

NTP_1970 = 2208988800
host = "pool.ntp.org"

ssid = '******'
password = '********'

def set_time():
    NTP_QUERY = bytearray(48)
    NTP_QUERY[0] = 0x1B
    addr = socket.getaddrinfo(host, 123)[0][-1]
    
    print(addr)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.settimeout(1)
        res = s.sendto(NTP_QUERY, addr)
        msg = s.recv(48)
    finally:
        s.close()
    val = struct.unpack("!I", msg[40:44])[0]
    t = val - NTP_1970    
    tm = time.gmtime(t)
    machine.RTC().datetime((tm[0], tm[1], tm[2], tm[6], tm[3], tm[4], tm[5], 0))

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

max_wait = 10
while max_wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    max_wait -= 1
    print('waiting for connection...')
    time.sleep(1)

if wlan.status() != 3:
    raise RuntimeError('network connection failed')
else:
    print('connected')
    status = wlan.ifconfig()
    print( 'ip = ' + status[0] )

set_time()
print(time.localtime())
led.off()

sda=machine.Pin(8)
scl=machine.Pin(9)
i2c=I2C(0,sda=sda, scl=scl, freq=400000)

display = ssd1306.SSD1306_I2C(128, 64, i2c)

while True:
    dateTime = time.localtime(time.time())
    #print("{:02d}-{:02d}-{:04d} {:02d}-{:02d}-{:02d}".format(dateTime[2],dateTime[1],dateTime[0],dateTime[3],dateTime[4],dateTime[5]))
    data = "{:02d}-{:02d}-{:04d}".format(dateTime[2],dateTime[1],dateTime[0])
    ora = "{:02d}-{:02d}-{:02d}".format(dateTime[3]+3,dateTime[4],dateTime[5])
    display.fill(0)
    display.text(data, 0, 0, 1)
    display.text(ora, 0, 10, 1)
    display.show()
    time.sleep(1)
