import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
coil_A_1_pin = 7 # purple
coil_A_2_pin = 8 # gray
coil_B_1_pin = 9 # ltgray
coil_B_2_pin = 10 # black

# adjust if different
StepCount = 8
Seq = list(range(0, StepCount))
Seq[0] = [1,0,0,0]
Seq[1] = [1,1,0,0]
Seq[2] = [0,1,0,0]
Seq[3] = [0,1,1,0]
Seq[4] = [0,0,1,0]
Seq[5] = [0,0,1,1]
Seq[6] = [0,0,0,1]
Seq[7] = [1,0,0,1]

# GPIO.setup(enable_pin, GPIO.OUT)
GPIO.setup(coil_A_1_pin, GPIO.OUT)
GPIO.setup(coil_A_2_pin, GPIO.OUT)
GPIO.setup(coil_B_1_pin, GPIO.OUT)
GPIO.setup(coil_B_2_pin, GPIO.OUT)

# GPIO.output(enable_pin, 1)

def setStep(w1, w2, w3, w4):
    GPIO.output(coil_A_1_pin, w1)
    GPIO.output(coil_A_2_pin, w2)
    GPIO.output(coil_B_1_pin, w3)
    GPIO.output(coil_B_2_pin, w4)
    
def forward(delay, steps):
    for i in range(steps):
        j = i%8
        setStep(Seq[j][0], Seq[j][1], Seq[j][2], Seq[j][3])
        time.sleep(delay)
            
def backwards(delay, steps):
    for i in range(steps):
        j = 7 - i%8
        setStep(Seq[j][0], Seq[j][1], Seq[j][2], Seq[j][3])
        time.sleep(delay)

if __name__ == '__main__':
    while True:
        setStep(0,0,0,0)
        delay = input("Time Delay (ms)? ")
        steps = input("How many steps forward? ")
        forward(int(delay) / 1000.0, int(steps))
        steps = input("How many steps backwards? ")
        backwards(int(delay) / 1000.0, int(steps))
        
