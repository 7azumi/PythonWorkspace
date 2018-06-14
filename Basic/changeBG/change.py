import win32con
import win32api
import win32gui
import time

'''
win32api.keybd_event(91,0,0,0)
time.sleep(0.1)
win32api.keybd_event(77,0,0,0)
time.sleep(0.2)
win32api.keybd_event(77,0,win32con.KEYEVENTF_KEYUP,0)
win32api.keybd_event(91,0,win32con.KEYEVENTF_KEYUP,0)

'''
win32api.SetCursorPos([500,300])
time.sleep(0.2)

win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0,0)
time.sleep(0.5)
win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0,0)
