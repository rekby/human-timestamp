#!/usr/bin/python3

import datetime
import signal
import notify2

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

last_clip_state = None

notification = notify2.Notification('')

start_since = datetime.datetime(1900, 1, 1).timestamp()


def is_int(s: str)->bool:
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
        if val == last_clip_state and val > start_since:
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
    notify2.init('human-timestamp')
    signal.signal(signal.SIGINT, signal.SIG_DFL)  # Exit on CTRL-C
    Gtk.main()


if __name__ == "__main__":
    main()


