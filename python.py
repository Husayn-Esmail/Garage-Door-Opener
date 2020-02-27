import time
import datetime
import picamera


print ("okay just a moment")
date_time = datetime.datetime.now()
str_today = str(date_time)
time.sleep(15)
camera = picamera.PiCamera()
camera.capture('Garagedoor.jpg')
print ("Here's your picture" + " Time : " + str_today)

