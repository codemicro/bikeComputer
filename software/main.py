import random
import sys
import threading
import time

import signal

import loops
from masterclass import m


def sigint_handler(_=None, __=None):
    print("Attempting gracefully shutting down...")

    # Make sure it actually clears
    m.disp.clear()
    m.disp.clear()
    m.disp.clear(release=False)

    sys.exit(0)


signal.signal(signal.SIGINT, sigint_handler)

display_thread = threading.Thread(target=loops.display_loop, daemon=True)
display_thread.start()

speed_thread = threading.Thread(target=loops.speed_monitor_loop, daemon=True)
speed_thread.start()

time.sleep(1)

m.ready = True

signal.pause()

# This will be useful later on
# while True:
#     draw.rectangle((0,0,DISPLAY_WIDTH,DISPLAY_HEIGHT), outline=0, fill=0)
#
#     if b.wait_for_press(timeout=5):
#         if last_active is None:
#             last_active = time.time()
#             draw.text((2, 2), "Speed: 0",  font=font, fill=255)
#         else:
#             speed = calculate_speed(time.time() - last_active)
#             last_active = time.time()
#             draw.text((2, 2), "Speed: " + str(int(speed)),  font=font, fill=255)
#     else:
#             draw.text((2, 2), "Speed: 0",  font=font, fill=255)
#
#     disp.image(image)
#     disp.display()
#     b.wait_for_release()
