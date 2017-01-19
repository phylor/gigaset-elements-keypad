import RPi.GPIO as GPIO

class Led:
  def __init__(self):
    self.led_red = 10
    self.led_green = 9
    self.led_blue = 11
    
    GPIO.setup(self.led_red, GPIO.OUT)
    GPIO.setup(self.led_green, GPIO.OUT)
    GPIO.setup(self.led_blue, GPIO.OUT)

  def red(self):
    GPIO.output(self.led_red, 1)
    GPIO.output(self.led_green, 0)
    GPIO.output(self.led_blue, 0)

  def orange(self):
    GPIO.output(self.led_red, 1)
    GPIO.output(self.led_green, 1)
    GPIO.output(self.led_blue, 0)

  def green(self):
    GPIO.output(self.led_red, 0)
    GPIO.output(self.led_green, 1)
    GPIO.output(self.led_blue, 0)
