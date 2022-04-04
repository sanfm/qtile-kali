#!/bin/bash

# Copy qtile.desktop in /usr/share/xsessions/
cp qtile.desktop /usr/share/xsessions/

# Add fonts
mkdir -p /usr/share/fonts/NerdFonts
cp fonts/NerdFiraCode.tar.gz /usr/share/fonts/NerdFonts/
tar -xf /usr/share/fonts/NerdFonts/NerdFiraCode.tar.gz -C /usr/share/fonts/NerdFonts
rm /usr/share/fonts/NerdFonts/NerdFiraCode.tar.gz
fc-cache -fv
