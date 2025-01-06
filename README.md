# Farstuns ansikte

**Links**
- https://shop.pimoroni.com/products/hyperpixel-4?variant=12569485443155
- https://highvoltages.co/iot-internet-of-things/mqtt/image-using-mqtt-protocol/
- https://pimylifeup.com/raspberry-pi-photo-frame/
- https://sr.ht/~exec64/imv/
- https://man.archlinux.org/man/imv.1.en
- https://manpages.debian.org/testing/imv/imv-wayland.5.en.html

**Steps**
- Install driver for Hyperpixel screen, instruction on pimoroni website, link above
- `sudo apt install imv python3-mqtt-paho` (Won't work with mqtt-paho version 2.0. Only works with 1.6.)
- Create services
  - `sudo nano /lib/systemd/system/face-get-image.service`
  - `sudo nano /lib/systemd/system/face-refresh-screen.service`

face-get-image.service
```
[Unit]
Description=Get image from double take mqtt and API
After=network.target

[Service]
Type=simple
ExecStart=/bin/python /home/llego/farstuns-ansikte/get-image.py
Restart=on-failure
RestartSec = 5
TimeoutStartSec = infinity
User=llego
Group=llego

[Install]
WantedBy=multi-user.target
```

face-refresh-screen.service
```
[Unit]
Description=Farstuns ansikte refresh screen
Wants=graphical.target
After=graphical.target

[Service]
Environment=DISPLAY=:0
Environment=XAUTHORITY=/home/llego/.Xauthority
Environment=XDG_RUNTIME_DIR=/run/user/1000
Type=simple
ExecStart=/bin/bash /home/llego/farstuns-ansikte/refresh-screen.sh
Restart=always
User=llego
Group=llego

[Install]
WantedBy=graphical.target
```

Enable and start services
```
sudo systemctl enable face-get-image.service --now
sudo systemctl enable face-refresh-screen.service --now
```


