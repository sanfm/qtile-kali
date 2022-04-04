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
  sudo apt install python3 python3-pip libpangocairo-1.0-0 betterlockscreen rofi lxpolkit -y
  ```

  ```sh
  pip3 install xcffib
  pip3 install --no-cache-dir cairocffi
  ```
  
  ```sh
  pip3 install qlite
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

5. Add a background image to betterlockscreen

  ```sh
  betterlockscreen -u <Path-to-picture>
  ```


## References

https://github.com/justinesmithies/qtile-wayland-dotfiles

https://github.com/justinesmithies/qtile-x-dotfiles

https://gitlab.com/dwt1/dotfiles/-/tree/master/.config/qtile

https://github.com/DaniDiazTech/Qtile-Config

https://github.com/sanfm/fm-debian





