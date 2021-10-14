import serial
from time import sleep

ser = serial.Serial ("/dev/ttyS0", 9600)    #Open port with baud rate
# while True:
data_left = ser.inWaiting()
a = bytes(bin(16), encoding="utf-8")

forward = b"100000000"
backward = b"010000000"
left = b"001000000"
rigth = b"000100000"
stop = b"000010000"
camera_up = b"000001000"
camera_down = b"000000100"
gripper_close = b"000000010"
gripper_open = b"000000001"



# print("forward")
# ser.write(forward)
# sleep(5)

# print("backward")
# ser.write(backward)
# sleep(5)
# ser.write(stop)


# print("left")
# ser.write(left)
# sleep(5)

# print("right")
# ser.write(rigth)
# sleep(5)
# ser.write(stop)

# print("stop")
# ser.write(sto)
# sleep(5)

# print("camera up")
# ser.write(camera_up)
# sleep(2)

# print("camera down")
# ser.write(camera_down)
# sleep(2)

# print("camera up")
# ser.write(camera_up)
# sleep(2)

# print("gripper open")
# ser.write(gripper_open)
# sleep(2)

print("gripper close")
ser.write(gripper_close)
sleep(7)

print("backward")
ser.write(backward)
sleep(3)
ser.write(stop)

# print(type(b'fsd'))
# print(type(bytes("fjsjd", 'utf-8')))