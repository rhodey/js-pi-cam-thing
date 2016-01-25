import sys
from time import sleep
from datetime import datetime
from pytz import timezone
from picamera import PiCamera

def takePictures(directory, interval):
  camera = PiCamera()
  while(True):
    dateNow  = datetime.now(timezone('US/Central'))
    filename = dateNow.strftime('%Y-%m-%d-%H-%M-%S') + '.jpg'
    camera.capture(directory + '/' + filename)
    sleep(interval)

if len(sys.argv) != 3:
  print("bad command line args")
  quit(1)

if not sys.argv[2].isdigit():
  print("bad command line args")
  quit(1)

takePictures(sys.argv[1], int(sys.argv[2]))

