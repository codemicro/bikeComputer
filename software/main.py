import sys

import signal

import loops
from masterclass import m


def sigint_handler(_=None, __=None):
    print("Attempting gracefully shutting down...")
    m.disp.clear()
    sys.exit(0)


signal.signal(signal.SIGINT, sigint_handler)


loops.loading_animation()


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
