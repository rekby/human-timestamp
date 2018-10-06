#!/usr/bin/python3

import datetime
import signal

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Notify', '0.7')
from gi.repository import Gtk, Gdk, Notify

APPNAME="Human timestamp"

last_clip_state = None

Notify.init(APPNAME)
notification = Notify.Notification()


def is_int(s)->bool:
    try:
        int(s)
    except ValueError:
        return False
    return True


def clipboard_updated(clipboard, _event):
    global last_clip_state
    text = clipboard.wait_for_text()  # type: str
    if is_int(text):
        val = int(text)
        if val == last_clip_state:
            summary = "human of {}".format(val)

            timevalue = datetime.datetime.fromtimestamp(val)
            human_text = timevalue.strftime("%Y-%m-%d %H:%M:%S")
            notification.update(summary, human_text)
            notification.show()
        last_clip_state = val
    else:
        last_clip_state = None


Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD).connect('owner-change', clipboard_updated)


def main():
    signal.signal(signal.SIGINT, signal.SIG_DFL)  # Exit on CTRL-C
    Gtk.main()


if __name__ == "__main__":
    main()


