'''MTTQ-Modbus-to-SQL-logger by Taki 2022'''

import sql_con
import mqtt_con
import time
import mariadb
import socket
import sys
import re
from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import sh1106
from PIL import ImageFont, ImageDraw, Image

#Display settings
bus = i2c(port=1, address=0x3C)
display = sh1106(bus)
font = ImageFont.truetype('FreeSans.ttf', 16)

#SQL connect
sql0 = sql_con.sql_config("logger.conf")

try:
    conn = mariadb.connect(
        user=sql0.user,
        password=sql0.passwd,
        host=sql0.host,
        port=int(sql0.port),
        database=sql0.db)
    
except mariadb.Error as e:
    with canvas(display) as draw:
        draw.text((10, 25), "SQL fault", font = font, fill = "white")
    print ("SQL connection failed")
    time.sleep(4)
    sys.exit(1)
    

print ("SQL  connection successful to "+sql0.host)

#MQTT connect
mqtt0 = mqtt_con.mqtt_config("logger.conf")
mqtt_client = mqtt0.create_client()

try:
    mqtt_client.connect(mqtt0.host)
    print ("MQTT connection successful to "+mqtt0.host)
    with canvas(display) as draw:
        draw.text((10, 10), "SQL done!", font = font, fill = "white")
        draw.text((10, 25), "MQTT done!", font = font, fill = "white")
        time.sleep(3)
        
except:
    print ("MQTT connection failed")
    with canvas(display) as draw:
        draw.text((10, 10), "SQL done!", font = font, fill = "white")
        draw.text((10, 25), "MQTT fault", font = font, fill = "white")
        


time.sleep(3)
exit()



