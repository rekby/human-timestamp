Human timestamp
===============

It is simple utility for see unix timestamp in human readable format.

Usage:

Add human-timestamp.py to startup on login, then copy timestamp to clipboard twice (CTRL-C, CTRL-C).
You will see balloon popup with human readable time in local timezone.

Add to startup, Gnome (ubuntu)
------------------------------
1. Copy human-timestamp.py to $PATH folder
2. Check exec rights: chmod +x human-timestamp.py
3. Copy human-timestamp.desktop to ~/.config/autostart/ folder

Dependencies
------------
GTK3, Notify 0.7

P.S.
----
It is work in my ubuntu 18.04, but not tested in clean system.

You are welcome to PR.
