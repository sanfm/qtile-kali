#!/bin/bash

# Make directories
mkdir -p ~/.config/qtile
mkdir -p ~/.cocnfig/rofi
mkdir -p ~/Pictures/wallpapers

# Copy config files
cp config/qtile/* ~/.config/qtile/
cp config/rofi/* ~/.cocnfig/rofi/

# Copy scripts to the $PATH
cp bin/* ~/.local/bin/

# Copy wallpapers
cp wallpapers/* ~/Pictures/wallpapers/

# Set a background for betterlockscreen
betterlockscreen -u ~/Pictures/wallpapers/wp-2.jpg
