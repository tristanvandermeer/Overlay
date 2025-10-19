import pynput
import time
import mss # Screen input


#------------------#
#
#To do:
#
#-> Plan out what its actually meant to do/farm
#-> Figure out how many layers of jitter/noise to add to movements
#-> Figure out how to deal with isometric view, and how best to do movement choices (Centering mouse, not being suspicious, planning route, then adding appropriate noise, calibrating location, etc)
#-> Brainstorm PVP bot :P
#
#------------------#

def set_up_func():
    pass

def loop_func():
    pass

#------------------#

def read_screen_region():
    time.sleep(3)
    monitor = {"top": 80, "left": 150, "width": 207, "height": 49}
    with mss.mss() as sct:
        sct_img = sct.grab(monitor)
        mss.tools.to_png(sct_img.rgb, sct_img.size, output="region_screenshot.png")

def get_stats():
    monitor = {"top": 80, "left": 150, "width": 207, "height": 49}
    with mss.mss() as sct:
        sct_img = sct.grab(monitor)
        mss.tools.to_png(sct_img.rgb, sct_img.size, output="stats_screenshot.png")

def create_goal():
    pass

def create_path():
    pass

def logout():
    pass

#------------------#

read_screen_region()