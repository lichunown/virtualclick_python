import threading, time, ctypes
import keyboard
from screen import screen_cut_and_get_point
from win import mouse_click, mouse_dclick


RUNNING_CLICK = False

def _async_raise(tid, exctype):
    """raises the exception, performs cleanup if needed"""
    tid = ctypes.c_long(tid)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")

def stop_thread(thread):
    _async_raise(thread.ident, SystemExit)
    

def running_click(point, click_func, delay=5):
    while True:
        if RUNNING_CLICK:
            mouse_click(*point)
        time.sleep(delay)
        
def change_button():
    global RUNNING_CLICK
    RUNNING_CLICK = not RUNNING_CLICK
    if RUNNING_CLICK:
        print('start click....')
    else:
        print('end click.')


if __name__ == '__main__':  
    import argparse
    
    parser = argparse.ArgumentParser(description='模拟鼠标点击，挂机刷')
    parser.add_argument('-t', '--type', type=str, default='click', help='单击或双击，单击：click，双击：dclick')
    parser.add_argument('-p', '--time', type=float, default='5', help='点击后的间隔时间')
    parser.add_argument('-b', '--button', type=str, default='n', help='开启或关闭点击的快捷键 ctrl+alt+[button]')
    args = parser.parse_args()

    if args.type == 'click':
        print('使用单击方法')
        click_fun = mouse_click
    elif args.type == 'dclick':
        print('使用双击方法')
        click_fun = mouse_dclick
    else:
        print('type: 只能为`click` or `dclick`')
        exit(0)
        
    if len(args.button) > 1:
        print('绑定快捷键 -b 参数只能为单个字符')
        exit(0)
        
    point = screen_cut_and_get_point()
    print("选定点：{}".format(point))
    t = threading.Thread(target=running_click, name='running_click', args=(point, click_fun, args.time))
    print("延迟：{}s".format(args.time))
    t.start()
    keyboard.add_hotkey('ctrl+alt+{}'.format(args.button), change_button)
    print('绑定开启关闭快捷键：{}'.format('ctrl+alt+{}'.format(args.button)))
    
    print('退出请按 ctrl+c')
    keyboard.wait('ctrl+c')
    stop_thread(t)