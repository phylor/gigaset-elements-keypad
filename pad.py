import sys
import RPi.GPIO as GPIO
import time
import yaml
from subprocess import call

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


def activate_alarm():
	call(['gigasetelements-cli', '-u', GIGASET_USER, '-p', GIGASET_PASSWORD, '-m', 'away'])
	return

def deactivate_alarm():
	call(['gigasetelements-cli', '-u', GIGASET_USER, '-p', GIGASET_PASSWORD, '-m', 'home'])
	return


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

while True:
	key = get_key()
	if key == '#':
		print('')
		if code == str(PIN):
			print('Deactivating alarm..')
			deactivate_alarm()
		code = ''
	elif key == '*':
		print('Activating alarm..')
		activate_alarm()
		code = ''
	elif key:
		code = code + key
		sys.stdout.write(key)
		sys.stdout.flush()
	time.sleep(0.3)

