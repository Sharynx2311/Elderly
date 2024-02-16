import pyautogui as PG
import numpy as np
import matplotlib.pyplot as plt

InputNumber = PG.prompt(text = 'Modulator, Carrier, Index, Time', title = 'Input').split(',')

modulator_frequency = float(InputNumber[0])
carrier_frequency = float(InputNumber[1])
modulation_index = float(InputNumber[2])
time_recorded = float(InputNumber[3])

time = np.arange(time_recorded) / time_recorded
modulator = np.cos(2.0 * np.pi * modulator_frequency * time) * modulation_index
carrier = np.cos(2.0 * np.pi * carrier_frequency * time)
product = np.zeros_like(modulator)

for i, t in enumerate(time):
    product[i] = np.cos(2. * np.pi * (carrier_frequency * t + modulator[i]))

plt.subplot(3, 1, 1)
plt.title('Frequency Modulation')
plt.plot(modulator, color = 'blue')
plt.ylabel('Amplitude')
plt.xlabel('Modulator signal')
plt.subplot(3, 1, 2)
plt.plot(carrier, color = 'red')
plt.ylabel('Amplitude')


plt.xlabel('Carrier signal')
plt.subplot(3, 1, 3)
plt.plot(product)
plt.ylabel('Amplitude')

plt.xlabel('Output signal')
plt.show()