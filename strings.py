import constants

# GUI
APPLICATION_TITLE = 'Among Us Report Bot'
INSTRUCTIONS = ('''Press Start to begin spamming the configured keystrokes.
Current keystrokes="{}"
The scale indicates delay between strokes in milliseconds.'''.format(constants.KEYS_TO_SEND))
START = 'START'
STOP = 'STOP'

# Console
LAUNCHING = ('''
=============================
Launching Among Us Report Bot
=============================
''')
PROC_FOUND = '\n> Found the target process: {} [pid={}]\n'
PROC_NOT_FOUND = '\n> Exiting application because the process named \"{}\" was not found. Please make sure that it is running.'.format(
    constants.PROC_NAME)
UNHANDLED_EXCEPTION = '\n> An unhandled exception occurred. Exiting application...'
LIST_PROCESSES = '> Listing processes on local machine:\n'
BOT_START = '> The bot has started'
BOT_STOP = '> The bot has stopped'
EXIT = '\nEXITING...'
