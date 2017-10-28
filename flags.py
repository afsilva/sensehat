#!/usr/bin/python
from sense_hat import SenseHat
import glob
import time
import os

sense = SenseHat()
sense.clear()
for filename in glob.iglob('icons/png-s/*.png'):
    try:
        base = os.path.basename(filename)
        sense.show_message("%s" % os.path.splitext(base)[0])
        sense.load_image("%s" % filename)
        time.sleep(0.5)
    except Exception:
        pass

