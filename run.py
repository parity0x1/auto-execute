#!/usr/bin/python3

import pyautogui
import time
import sys
from pynput import keyboard

def welcome():
    print ("                            __               __             _      ")
    print ("                         __/\ \__          /'__`\         /' \     ")
    print (" _____      __     _ __ /\_\ \ ,_\  __  __/\ \/\ \  __  _/\_, \    ")
    print ("/\ '__`\  /'__`\  /\`'__\/\ \ \ \/ /\ \/\ \ \ \ \ \/\ \/'\/_/\ \   ")
    print ("\ \ \L\ \/\ \L\.\_\ \ \/ \ \ \ \ \_\ \ \_\ \ \ \_\ \/>  </  \ \ \  ")
    print (" \ \ ,__/\ \__/.\_\\ \_\  \ \_\ \__\\/`____ \ \____//\_/\_\  \ \_\ ")
    print ("  \ \ \/  \/__/\/_/ \/_/   \/_/\/__/ `/___/> \/___/ \//\/_/   \/_/ ")
    print ("   \ \_\                                /\___/                     ")
    print ("    \/_/                                \/__/                      ")
    print ("                                                autoexecute alpha  ")
    print()
    print("<ctrl>+<alt>+s - Stabalize reverse shell using Python 3")
    print("<ctrl>+<alt>+q - Exit/Quit")
    print()


def wait():
    time.sleep(5)


def stabilize_shell():
    print ('Stabilizing shell using Python3')
    wait()
    pyautogui.typewrite("python3 -c 'import pty; pty.spawn(\"/bin/bash\");'")
    wait()
    pyautogui.hotkey('enter')
    pyautogui.hotkey('ctrl','z')
    pyautogui.typewrite("stty raw -echo")
    pyautogui.hotkey('enter')
    pyautogui.typewrite("fg")
    pyautogui.hotkey('enter')
    pyautogui.typewrite("export TERM=xterm")
    pyautogui.hotkey('enter')

def on_activate_s():
    stabilize_shell()

welcome()

with keyboard.GlobalHotKeys({'<ctrl>+<alt>+s': on_activate_s}) as h:
    h.join()