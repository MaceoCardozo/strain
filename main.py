from pync import Notifier
import time
import os
import sys
from datetime import datetime, timedelta
import schedule
# program main
def main():
    notification()
    sleep_computer()

# sleep function
def sleep_computer():
    os.system("osascript -e 'tell application \"Finder\" to sleep'")

def str_2_bool(value):
        return value.lower() in ("yes", "true", "t", "1")

# notification
def notification():
    Notifier.notify("HEY THERE, ITS TIME TO LOOK AWAY", title='LOOK AWAY', sound='Glass',appIcon='https://icons.iconarchive.com/icons/custom-icon-design/mono-general-4/512/eye-icon.png')

# p10rogram run
if __name__ == '__main__':
    while (True):
            secs = input('HOW LONG DO YOU WANT TO LOOK AT YOUR SCREEN?\n')
            print('LOOK AWAY AFTER', secs, 'seconds.')
            time.sleep(float(secs))
            notification()
            time.sleep(3)
            sleep_computer()
            sys.exit()








