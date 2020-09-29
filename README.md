# Openbox Menu
Tested with Openbox 3.6.1

Require Python3-xdg.

This is a python3 script that generates a menu for Openbox from the desktop files.
This program search for the desktop files in the /usr/share/applications and
in the HOME/.local/share/applications directories.
The entries in the menu follow the freedesktop categories names.

How to use: python3 make_ob_menu.py > menu.xml
Copy the menu.xml file in $HOME/.config/openbox (eventually replace the old one).
Reload the configuration: openbox --reconfigure

The screenshot is how the menu looks like

![My image](https://github.com/frank038/Openbox_menu/blob/master/img1.jpg)
