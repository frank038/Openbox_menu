#!/bin/bash

thisdir=$(dirname "$0")
cd $thisdir

./make_ob_menu.py > menu.xml
mv ~/.config/openbox/menu.xml ~/.config/openbox/menu.xml-old
mv menu.xml ~/.config/openbox
