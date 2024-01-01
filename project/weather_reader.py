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
temp_lin = []
time = []

list_timestamp = []

for i in range(len(unit_list)):
    if unit_list[i] == "C":
        temp.append(sensor_ids[i])
    if unit_list[i] == "%":
        hum.append(sensor_ids[i])
print(temp, hum)

for reading_c in p:
    if reading_c['sensor_id'] in temp:
        print(reading_c)
        print(reading_c['value'])
        if 12757 <= int(reading_c['id']) <= 21088:
            if int(reading_c['sensor_id']) == 0:
                temp_48hrs_data_id0.append(reading_c['value'])
                temp_lin.append(reading_c['value'])

            elif int(reading_c['sensor_id']) == 1:
                temp_48hrs_data_id1.append(reading_c['value'])
                temp_lin.append(reading_c['value'])

            else:
                temp_48hrs_data_id2.append(reading_c['value'])
                temp_lin.append(reading_c['value'])


for reading_hum in p:
    if reading_hum['sensor_id'] in hum:
        print(reading_hum)
        print(reading_hum['value'])

        if 12760 <= int(reading_hum['id']) <= 21089:
            if int(reading_hum['sensor_id']) == 4:
                hum_48hrs_data_id4.append(reading_hum['value'])
                datetime_string = reading_hum['datetime']
            else:
                hum_48hrs_data_id5.append(reading_hum['value'])


print(temp_48hrs_data_id0)
print(temp_48hrs_data_id1)
print(temp_48hrs_data_id2)
print(hum_48hrs_data_id4)
print(hum_48hrs_data_id5)
print(len(hum_48hrs_data_id4))
print("id0, id1, id2, id4, id5, end")
print(list_timestamp)

hum_ave = []
for i in range(len(hum_48hrs_data_id4)):
    hum_ave.append((hum_48hrs_data_id4[i]+hum_48hrs_data_id5[i])/2)

temp_ave = []
for i in range(len(temp_48hrs_data_id0)):
    temp_ave.append((temp_48hrs_data_id0[i]+temp_48hrs_data_id1[i]+temp_48hrs_data_id2[i])/3)

#list_timestamp = [datetime.strptime(reading_c['datetime'], '%Y-%m-%dT%H:%M:%S.%f').timestamp() for reading_c in p if reading_c['sensor_id'] in temp]

temp = []
time = []

with open ('weather.csv', mode='r') as f:
    csv_reader = csv.DictReader(f)
    for row in csv_reader:
        temp_2 = row['Humidity']
        temp_2 = float(temp_2)
        temp.append(temp_2)
        time.append(5*len(temp))

std = []
for d in temp_ave:
    std.append(np.std(d))

x, y = smoothing(values=hum_ave)
a, b = smoothing(values=temp_ave)
c, d = smoothing(values=temp)

#plt.plot(x, y, color="black")
#plt.axhline(y=max(y), color="red")
#plt.axhline(y=min(y), color="orange")
#plt.axhline(y=np.mean(y), color="blue")
plt.errorbar(x, y, std, fmt="o", color="#023047")
plt.fill_between(x, y, alpha=0.5, linewidth=0, color="#8ecae6")
plt.legend()
plt.title("Outdoor humidity")
plt.xlabel("minutes")
plt.ylabel("%")
#plt.gca().xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%Y-%m-%d %H:%M:%S'))
plt.xticks(rotation=45)
plt.show()
