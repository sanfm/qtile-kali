#!/bin/bash

# Make directories
mkdir -p ~/.config/qtile
mkdir -p ~/.config/rofi
mkdir -p ~/Pictures/wallpapers

# Copy config files
cp -r config/qtile/* ~/.config/qtile/
cp -r config/rofi/* ~/.config/rofi/

# Copy scripts to the $PATH
cp -r bin/* ~/.local/bin/

# Copy wallpapers
cp -r wallpapers/* ~/Pictures/wallpapers/

# Set a background for betterlockscreen
betterlockscreen -u ~/Pictures/wallpapers/wp-2.jpg
