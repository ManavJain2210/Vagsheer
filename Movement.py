import pigpio
import time
pi = pigpio.pi()

def forward(sec):
    pi.set_servo_pulsewidth(4, 2000) # Minimum throttle.
    pi.set_servo_pulsewidth(17, 2000)
    time.sleep(sec)

def left(sec):
    pi.set_servo_pulsewidth(4, 2000) # Minimum throttle.
    pi.set_servo_pulsewidth(17, 2000)
    time.sleep(sec)

def right(sec):
    pi.set_servo_pulsewidth(4, 2000) # Minimum throttle.
    pi.set_servo_pulsewidth(17, 2000)
    time.sleep(sec)

def reverse(sec):
    pi.set_servo_pulsewidth(4, 2000) # Minimum throttle.
    pi.set_servo_pulsewidth(17, 2000)
    time.sleep(sec)

def dive(sec):
    pi.set_servo_pulsewidth(4, 2000) # Minimum throttle.
    pi.set_servo_pulsewidth(17, 2000)
    time.sleep(sec)

def main():


main()
