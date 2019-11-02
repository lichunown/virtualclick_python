from PIL import ImageGrab
from matplotlib import pylab
import keyboard
import argparse
import time, threading

from win import screen_resolution, mouse_click


    

RUNNING_CLICK = False

def running_click(point,delay=5):
    while True:
        if RUNNING_CLICK:
            mouse_click(*point)
        time.sleep(delay)
        
def change_button():
    global RUNNING_CLICK
    RUNNING_CLICK = not RUNNING_CLICK
    if RUNNING_CLICK:
        print('start click point ({},{}), {}s/times')
    else:
        print('end click point ({},{}), {}s/times')
    
if __name__ == "__main__":
#    screen_img = screen_capture()
#    point = show_image_and_get_point(screen_img)
#    print(point)
#    t = threading.Thread(target=running_click, name='running_click', args=(point, ))
#    t.start()
    keyboard.add_hotkey('ctrl+alt+n', change_button)
#    
#    
    
    
    
    
    
    
    
    