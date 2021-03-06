# qtile-kali

A qtile environment for kali

----------------------------------------

## Requirements

* Python3
* Pip
* Rofi
* Betterlockscreen
* Lxpolkit
* libpangocairo-1.0-0
* Qtile


  ```sh
  sudo apt install python3 python3-pip libpangocairo-1.0-0 betterlockscreen rofi lxpolkit picom -y
  ```

  ```sh
  pip3 install xcffib
  pip3 install --no-cache-dir cairocffi
  pip install psutil
  ```
  
  ```sh
  pip3 install qtile
  ```
  
## Istallation

1. Install the requirements

2. Clone the repo

  ```sh
  git clone https://github.com/sanfm/qtile-kali.git
  cd qtile-kali
  ```
  
3. Run setup.sh (as root)

  ```sh
  sudo sh setup.sh
  ```

4. Run config.sh (as $USER)

  ```sh
  sh config.sh
  ```



Read "*Things to consider*" and you're ready to restart and login selecting qtile as your window manager.

### Things to consider

1. if you use a user other than kali, you have to edit the qtile.desktop file in order to change the path to your user's

  ```sh
  sudo vim /usr/share/xsessions/qtile.desktop
  ```
Change the line: 

* Exec=/home/kali/.local/bin/qtile start

for:

* Exec=/home/user-name/.local/bin/qtile start


2. Select the path to the wallpaper in the file ~/.config/qtile/autostart.sh

In that file you have to set the correct path to the wallpaper you want feh to use


3. Change the lock screen background


  ```sh
  betterlockscreen -u <Path-to-picture>
  ```


4. Changing font size

If you think the font size is too small (or too big), you can change it in qtile's config file (/home/user-name/.config/qtile/config.py) and in rofi's configuration (/home/user-name/.config/rofi/config.rasi ando also in the rofi's themes files /home/user-name/.config/rofi/themes)
  

## References

https://github.com/justinesmithies/qtile-wayland-dotfiles

https://github.com/justinesmithies/qtile-x-dotfiles

https://gitlab.com/dwt1/dotfiles/-/tree/master/.config/qtile

https://github.com/DaniDiazTech/Qtile-Config

https://github.com/sanfm/fm-debian





