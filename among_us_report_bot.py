# Run "pip install pywin32 psutil tkinter"
import time
import threading
import sys
import psutil
from send_keys_thread import SendKeysThread
import strings
import constants
from tkinter import (Tk, Label, Button,  Scale,
                     StringVar, HORIZONTAL, W, EW)


class AmongUsReportBot(Tk):
    def __init__(self):
        Tk.__init__(self)

        # Process ID of the target process
        self.__pid = self.__get_pid()

        # Initialize window properties
        self.title(strings.APPLICATION_TITLE)

        # Instruction label
        Label(self, text=strings.INSTRUCTIONS).grid(row=0, column=0)

        # Delay scale
        self.delay_scale = Scale(self, from_=1, to=1000, orient=HORIZONTAL)
        self.delay_scale.grid(row=1, column=0, sticky=EW)

        # Start / Stop button
        self.button_text = StringVar(value=strings.START)
        self.button = Button(self,
                             bg="pale green",
                             textvariable=self.button_text,
                             command=self.__on_button_press)
        self.button.grid(row=2, column=0, sticky=EW)

        # Thread for sending keys
        self.__subprocess = SendKeysThread(
            keys=constants.KEYS_TO_SEND,
            delay=self.delay_scale.get())

    def __get_pid(self):
        # This function is pretty useless but looks cool
        pid = -1
        print(strings.LIST_PROCESSES)

        try:
            for proc in psutil.process_iter():
                try:
                    print("{} [pid={}]".format(proc.name(), proc.pid))

                    # Found the target process
                    if proc.name() == constants.PROC_NAME:
                        pid = proc.pid
                        break

                # Some processes may deny access
                except psutil.AccessDenied:
                    pass

            # Could not find target process
            if pid == -1:
                raise ProcessLookupError

            # If we made it this far, then the target process has been found
            print(strings.PROC_FOUND.format(constants.PROC_NAME, pid))
            return pid

        except ProcessLookupError:
            print(strings.PROC_NOT_FOUND)
            sys.exit()

        except:
            print(strings.UNHANDLED_EXCEPTION)
            sys.exit()

    def __on_button_press(self):
        # Create subprocess if it does not exist yet
        if self.__subprocess is None:
            self.__subprocess = SendKeysThread(
                keys=constants.KEYS_TO_SEND,
                delay=self.delay_scale.get())

        if not self.__subprocess.signal:
            # Visual updates for the button
            self.button.configure(bg="salmon")
            self.button_text.set(strings.STOP)

            # Start subprocess
            self.__subprocess.signal = True
            threading.Thread(target=self.__subprocess.run).start()
            print(strings.BOT_START)

        else:
            # Visual updates for the button
            self.button.configure(bg="pale green")
            self.button_text.set(strings.START)

            # Stop subprocess
            self.__subprocess.signal = False
            print(strings.BOT_STOP)

    def on_closing(self):
        # Handler for closing the GUI
        print(strings.EXIT)
        self.__subprocess.signal = False
        self.destroy()


def main():
    print(strings.LAUNCHING)
    app = AmongUsReportBot()
    app.protocol('WM_DELETE_WINDOW', app.on_closing)
    app.mainloop()


if __name__ == '__main__':
    main()
