import numpy as np
import requests
import csv
import matplotlib
import matplotlib.pyplot as plt
from datetime import datetime
from lib_api import smoothing, get_data_from_date
from lib_api_2 import sensor_ids
from lib_api_2 import unit_list

plt.style.use('ggplot')
matplotlib.use('MacOSX')

request = requests.get(f'http://192.168.6.153/readings')
data = request.json()

p = data['readings'][0]

temp = []
hum = []
temp_48hrs_data_id0 = []
temp_48hrs_data_id1 = []
temp_48hrs_data_id2 = []
hum_48hrs_data_id4 = []
hum_48hrs_data_id5 = []

list_timestamp = []

for i in range(len(unit_list)):
    if unit_list[i] == "C":
        temp.append(sensor_ids[i])
    if unit_list[i] == "%":
        hum.append(sensor_ids[i])

for reading_c in p:
    if reading_c['sensor_id'] in temp:
        if 12757 <= int(reading_c['id']) <= 21088:
            if int(reading_c['sensor_id']) == 0:
                temp_48hrs_data_id0.append(reading_c['value'])
            elif int(reading_c['sensor_id']) == 1:
                temp_48hrs_data_id1.append(reading_c['value'])
            else:
                temp_48hrs_data_id2.append(reading_c['value'])

for reading_hum in p:
    if reading_hum['sensor_id'] in hum:
        if 12760 <= int(reading_hum['id']) <= 21089:
            if int(reading_hum['sensor_id']) == 4:
                hum_48hrs_data_id4.append(reading_hum['value'])
            else:
                hum_48hrs_data_id5.append(reading_hum['value'])

hum_ave = [(h4 + h5) / 2 for h4, h5 in zip(hum_48hrs_data_id4, hum_48hrs_data_id5)]
temp_ave = [(t0 + t1 + t2) / 3 for t0, t1, t2 in zip(temp_48hrs_data_id0, temp_48hrs_data_id1, temp_48hrs_data_id2)]

#list_timestamp = [datetime.strptime(reading_c['datetime'], '%Y-%m-%dT%H:%M:%S.%f').timestamp() for reading_c in p if reading_c['sensor_id'] in temp]

temp = []
time = []

with open('weather.csv', mode='r') as f:
    csv_reader = csv.DictReader(f)
    for row in csv_reader:
        temp_2 = row['Humidity']
        temp_2 = float(temp_2)
        temp.append(temp_2)
        time.append(5 * len(temp))

# Calculate standard deviation for the fill_between
std_temp = np.std(temp_ave)

# Plotting
x, y = smoothing(values=hum_ave)
a, b = smoothing(values=temp_ave)
c, d = smoothing(values=temp)

#plt.plot(c, d, color="black")
#plt.axhline(y=max(d), color="red")
#plt.axhline(y=min(d), color="orange")
#plt.axhline(y=np.mean(d), color="blue")

# Modified section
m, z = np.polyfit(x, y, 1)
print(f"Linear Model is T(t) = {m}t + {z}")

time_model = []
temp_model = []
for i in range(len(temp_ave)):
    time_model.append(i)
    temp_model.append(m*i + z)

plt.plot(time_model, temp_model, label="Linear model")
plt.plot(x, y, label="original curve")
plt.title("Linear model for outdoor temperature")
plt.xlabel("Minutes")
plt.ylabel("celcius")
plt.legend()
plt.show()

# Print the standard deviation
print(f"Standard Deviation of Outdoor Humidity: {std_temp}")
