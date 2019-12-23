from datetime import datetime


def print_with_time(message, indents=0):
    """Print something with time before it

    Arguments:
        message {string} -- message that will be printed to the console
        color {string} -- color of the text printed to the console
        indents {int} -- number of 3 tabs
    """
    current_time = str(datetime.now())
    tabs = []
    for i in range(indents):
        tabs.append("\t")
    print(current_time, "|", "".join(tabs) + message)
