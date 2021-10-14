import RPi.GPIO as GPIO 
from time import sleep


GPIO.setmode(GPIO.BCM)
# GPIO.setup(4, GPIO.OUT, initial=GPIO.LOW)
# GPIO.setup(5, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(6, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(23, GPIO.OUT, initial=GPIO.LOW)
# GPIO.setup(24, GPIO.OUT, initial=GPIO.LOW)

duration = 10

# for _ in range(1):

# print("left")
# GPIO.output(5, 1)
# sleep(duration)
# print("left stop")
# GPIO.output(5, 0)
# sleep(duration)

# print("right")
# GPIO.output(6, 1)
# sleep(duration)
# print("right stop")
# GPIO.output(6, 0)
# sleep(duration)


GPIO.output(23, 1)
print("forward run")
sleep(10)
print("forward stop")
# GPIO.output(23, 0)
GPIO.output(6, 1)
sleep(10)
# print("exit")
# GPIO.output(6, 0)
# GPIO.output(23, 0)



# while True:
#     try:
#         print("forward")
#     except KeyboardInterrupt:
#         print("stop")
#         GPIO.output(5, 0)
#         break

# sleep(duration)
# print("forward stop")
# GPIO.output(23, 0)
# sleep(duration)


# print("backward")
# GPIO.output(24, 1)
# sleep(duration)
# print("backward stop")
# GPIO.output(24, 0)
# sleep(duration)