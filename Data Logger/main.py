'/dev/cu.usbmodem141101'
import serial
import time
import pandas as pd
import matplotlib.pyplot as plt

# parammters
serial_port = '/dev/cu.usbmodem141101'  # Change this to match the port where your Arduino is connected
baud_rate = 9600  # Adjust baud rate as needed
scanTime = 5
scanData = []

# Initialize serial port
ser = serial.Serial(serial_port, baud_rate, timeout = 1)
time.sleep(0.5)

# Read data from Arduino
readings = []
elapsed = []
start_time = time.time()
while time.time() - start_time < scanTime:
    r = ser.readline().decode().strip()
    if r:
        t = time.time() - start_time
        r = int(r)
        readings.append(r)
        elapsed.append(t)
        print("Elapsed Time: {:.2f} | Reading: {:.2f}".format(t, r), end='\r')
ser.close() # Close serial port

# Process data as needed
df = pd.DataFrame({'elapsed': elapsed, 'readings': readings})
df['dwell_S'] = df['elapsed'].diff()
print(df.describe())
df.to_csv("data.csv")

# Basics
plt.plot(df['elapsed'], df['readings'])
plt.show()