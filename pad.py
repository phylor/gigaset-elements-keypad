import sys
import RPi.GPIO as GPIO
import time
import yaml
import display
import led
from gigaset_elements import GigasetElements
from threading import Timer

GPIO.setmode(GPIO.BCM)

GIGASET_USER = ''
GIGASET_PASSWORD = ''
PIN = ''

stream = open('settings.yml', 'r')
settings = yaml.load(stream)
for k,v in settings.items():
	if k == 'user':
		GIGASET_USER = v
	elif k == 'password':
		GIGASET_PASSWORD = v
	elif k == 'pin':
		PIN = v




# pin layout (1 is the left most pin on the keypad):
# 1: GPIO18
# 2: GPIO17
# 3: GPIO27
# 4: GPIO23
# 5: GPIO22
# 6: GPIO24
# 7: GPIO25

rows = [17, 25, 24, 23]
cols = [27, 18, 22]
keys = [
	['1', '2', '3'],
	['4', '5', '6'],
	['7', '8', '9'],
	['*', '0', '#']]

for row_pin in rows:
	GPIO.setup(row_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

for col_pin in cols:
	GPIO.setup(col_pin, GPIO.OUT)

def get_key():
	key = 0
	for col_num, col_pin in enumerate(cols):
		GPIO.output(col_pin, 1)
		for row_num, row_pin in enumerate(rows):
			if GPIO.input(row_pin):
				key = keys[row_num][col_num]
		GPIO.output(col_pin, 0)
	return key

code = ''
lcd = display.Display()
gigaset = GigasetElements(GIGASET_USER, GIGASET_PASSWORD)
led = led.Led()

def show_status():
	status = gigaset.alarm_status()
	lcd.clear()
	lcd.message('Alarm\n' + status)
	
	if status == 'away':
		led.red()
	elif status == 'home':
		led.green()

def start_status_timer():
	show_status()
	alarm_status_timer = Timer(5 * 60, start_status_timer)
	alarm_status_timer.start()
	
led.orange()
start_status_timer()


while True:
	key = get_key()
	if key == '#':
		lcd.clear()
		if code == str(PIN):
			lcd.message('Alarm\ndeactivating..')
			led.orange()
			gigaset.deactivate_alarm()
		
		code = ''
		show_status()
	elif key == '*':
		lcd.clear()
		lcd.message('Alarm\nactivating..')
		led.orange()
		gigaset.activate_alarm()
		code = ''
		show_status()
	elif key:
		code = code + key
		lcd.clear()
		lcd.message(code)
	
	time.sleep(0.3)

