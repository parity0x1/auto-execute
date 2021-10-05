#!/usr/bin/python3

import pyautogui
import time
import signal
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
    print("<ctrl>+<alt>+1 - Stabilize reverse shell using Python 3")
    print("<ctrl>+<alt>+2 - Search for SUID")
    print("<ctrl>+<alt>+q - Exit/Quit")
    print()


def wait():
    time.sleep(5)


def pause():
    time.sleep(2)


def stabilize_shell():
    print ('Ready to stabilize shell using Python3. Click on target window now...')
    wait()
    pyautogui.typewrite("python3 -c 'import pty; pty.spawn(\"/bin/bash\");'")
    pause()
    pyautogui.hotkey('enter')
    pyautogui.hotkey('ctrl','z')
    pyautogui.typewrite("stty raw -echo")
    pyautogui.hotkey('enter')
    pyautogui.typewrite("fg")
    pyautogui.hotkey('enter')
    pyautogui.typewrite("export TERM=xterm")
    pyautogui.hotkey('enter')


def suid():
    print ('Ready to search for SUID. Click on target window now...')
    wait()
    pyautogui.typewrite("find / -perm -4000 2>/dev/null")
    pause()
    pyautogui.hotkey('enter')


def exit():
    sys.exit(0)


def signal_handler(sig, frame):
    exit()

signal.signal(signal.SIGINT, signal_handler)

welcome()

with keyboard.GlobalHotKeys({
    '<ctrl>+<alt>+1':stabilize_shell,
    '<ctrl>+<alt>+2':suid,
    '<ctrl>+<alt>+q':exit
    }) as listener:
    listener.join()