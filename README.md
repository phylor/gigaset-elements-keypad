## Installation

    sudo pip install RPi.GPIO
    sudo pip install gigasetelements-cli
    sudo pip install pyyaml
    git clone https://github.com/adafruit/Adafruit_Python_CharLCD
    cd Adafruit_Python_CharLCD
    sudo python setup.py install

## Usage

Create a `settings.yml` with the following contents:

    user: gigaset@example.com
    password: secret
    pin: 1234

- Activate alarm: `*` key
- Deactivate alarm: enter PIN followed by `#` key

Run it:

    sudo python pad.py

## Components

- Sparkfun COM-08653 12-key keypad
