import constants
import threading
import time
import win32com.client
from win32gui import GetWindowText, GetForegroundWindow

# The shell sends keys
shell = win32com.client.Dispatch('WScript.Shell')


class SendKeysThread(threading.Thread):
    def __init__(self, keys, delay):
        threading.Thread.__init__(self)
        self.keys = keys
        self.delay = delay
        self.signal = False

    def run(self):
        while self.signal:
            if GetWindowText(GetForegroundWindow()) == constants.APP_NAME:
                shell.SendKeys(self.keys)
                time.sleep(self.delay / 1000)
            else:
                # Wait for app to be in foreground
                print("> Paused...waiting for target application to be in foreground")
                while self.signal and GetWindowText(GetForegroundWindow()) != constants.APP_NAME:
                    pass

                if self.signal:
                    print("> Sending keys: {}".format(constants.KEYS_TO_SEND))
