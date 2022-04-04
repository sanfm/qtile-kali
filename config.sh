#!/bin/bash

# Make directories
mkdir -p ~/.config/qtile
mkdir -p ~/.config/rofi
mkdir -p ~/Pictures/wallpapers

# Copy config files
cp -r config/qtile/* ~/.config/qtile/
cp -r config/rofi/* ~/.config/rofi/
cp config/picom.conf ~/.config

# Copy scripts to the $PATH
cp -r bin/* ~/.local/bin/

chmod 744 ~/.local/bin/lockscreen.sh
chmod 744 ~/.local/bin/powermenu
chmod 744 ~/.config/qtile/autostart.sh

# Copy wallpapers
cp -r wallpapers/* ~/Pictures/wallpapers/

# Set a background for betterlockscreen
betterlockscreen -u ~/Pictures/wallpapers/wp-2.jpg
