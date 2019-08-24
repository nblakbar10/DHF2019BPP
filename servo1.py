import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(7,GPIO.OUT)

p = GPIO.PWM(7,50)
p.start(7.5)

try:
	while True:
		p.ChangeDutyCycle(7)
		time.sleep(0.5)
		p.ChangeDutyCycle(7)
		time.sleep(0.5)
		p.ChangeDutyCycle(7)
		time.sleep(0.5)

except KeyboardInterrupt:
	p.stop()

	GPIO.cleanup()
