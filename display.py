import Adafruit_CharLCD as LCD


class Display:

	def __init__(self):
  	    # Raspberry Pi pin configuration:
  	    lcd_rs = 21
  	    lcd_en = 20
  	    lcd_d4 = 16
  	    lcd_d5 = 13
  	    lcd_d6 = 19
  	    lcd_d7 = 26
  	    
  	    # Define LCD column and row size for 16x2 LCD.
  	    lcd_columns = 16
  	    lcd_rows    = 2
  	    
  	    # Initialize the LCD using the pins above.
  	    self.lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,
                                 lcd_columns, lcd_rows)

	def clear(self):
		self.lcd.clear()

	def message(self, message_to_display):
		self.lcd.message(message_to_display)
