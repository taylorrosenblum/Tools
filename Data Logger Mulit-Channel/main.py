import serial
import time
import pandas as pd
import matplotlib.pyplot as plt

# parameters
serial_port = '/dev/cu.usbmodem143101'  # Change this to match the port where your Arduino is connected
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
        arr = r.split(',')
        elapsed.append(t)
        readings.append(arr)
        print("Elapsed Time: {:.2f} | "
              "Ch0: {:.2f} | "
              "Ch1: {:.2f} | "
              "Ch2: {:.2f}".format(t, int(arr[0]), int(arr[1]), int(arr[2])),
              end='\r')
ser.close() # Close serial port

# slice data in to individual channels
ch0 = []
ch1 = []
ch2 = []
for row in readings:
    row = list(row)
    ch0.append(int(row[0]))
    ch1.append(int(row[1]))
    ch2.append(int(row[2]))

# Process data as needed
df = pd.DataFrame({'elapsed': elapsed,
                   'ch0': ch0,
                   'ch1': ch1,
                   'ch2': ch2})
df['sample_interval'] = df['elapsed'].diff()
print(df.describe())
df.to_csv("data.csv")

# Simple plotting
plt.plot(df['elapsed'], df['ch0'],alpha=0.75,label='ch0')
plt.plot(df['elapsed'], df['ch1'],alpha=0.75,label='ch1')
plt.plot(df['elapsed'], df['ch2'],alpha=0.75,label='ch2')
plt.xlabel('time_elapsed_s')
plt.legend()
plt.show()