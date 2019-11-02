from PIL import ImageGrab
from matplotlib import pylab

from win import screen_resolution


def screen_capture():
    width, height = screen_resolution()    
    image = ImageGrab.grab((0, 0, width, height))
    return image


def screen_cut_and_get_point():
    screen_img = screen_capture()
    pylab.figure(1, tight_layout=True)
    pylab.axis('off')
    pylab.imshow(screen_img)
    mng = pylab.get_current_fig_manager()
    mng.window.showMaximized()
    mng.set_window_title('请用鼠标点击希望模拟鼠标点击的区域')
    point = pylab.ginput(1)[0]
    pylab.close()
    return point