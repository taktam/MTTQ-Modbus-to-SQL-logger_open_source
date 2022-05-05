import sql_con
import time
import mariadb
import socket
import sys
import re
from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import sh1106
from PIL import ImageFont, ImageDraw, Image

serial = i2c(port=1, address=0x3C)
device = sh1106(serial)
oled_font = ImageFont.truetype('FreeSans.ttf', 14)

con0 = sql_con.load_config("logger.conf")

try:
    conn = mariadb.connect(
        user=con0.user,
        password=con0.passwd,
        host=con0.host,
        port=int(con0.port),
        database=con0.db
    )
except mariadb.Error as e:
    with canvas(device) as draw:
        draw.text((10, 10), "SQL connection ", font = oled_font, fill = "white")
        draw.text((10, 25), "      is failed", font = oled_font, fill = "white")
        print ("SQL connection failed")
        print ('\n'+e)
    sys.exit(1)
    


with canvas(device) as draw:
    draw.text((10, 10), "SQL connection ", font = oled_font, fill = "white")
    draw.text((10, 25), "  is successful", font = oled_font, fill = "white")
    print ("SQL connection successful to "+con0.host)
    
time.sleep(5)
exit()



