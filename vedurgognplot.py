import numpy as np
import matplotlib.pyplot as plt

import urllib.request, json
# Thurfum pakkana json og urllib.request til ad saekja og lesa gognin

uppl_url = 'http://apis.is/weather/observations/is?stations=1,422,571,620'
spa_url = 'http://apis.is/weather/forecasts/is?stations=1,422,571'
# Her er verid ad saekja vedurspar fyrir Reykjavik

# Notum urlopen fallid til ad saekja upplysingar af netinu
u_response = urllib.request.urlopen(uppl_url)
s_response = urllib.request.urlopen(spa_url)

# Notum json.loads fallid til ad lesa json gogn yfir i python dictionary
uppl_data = json.loads(u_response.read().decode('utf8'))
spa_data = json.loads(s_response.read().decode('utf8'))

# Prentum ut gognin til ad sja hvernig thau lita ut
#print(uppl_data['results'][3])

#for i in range(0,3):
#	print('Stadsetning:',uppl_data['results'][i]['name'])
	#print('Hitastig:',uppl_data['results'][i]['forecast'][0]['T'])
fig1 = plt.figure()
#line.set_data()
data1 = []
time1 = []
for i in range(0,24):
	data1.append(spa_data['results'][0]['forecast'][i]['T']) 
	time1.append(i)
	#time1.append(spa_data['results'][0]['forecast'][i]['ftime'][11:13])
#print(data1)
#print(time1)
data2 = []
time2 = []
for j in range(0,24):
	data2.append(spa_data['results'][1]['forecast'][j]['T'])
	time2.append(j)
	#time2.append(spa_data['results'][1]['forecast'][j]['ftime'][11:13])
#print(data2)
#print(time2)
data3 = []
time3 = []
xas1 = []
for k in range(0,24):
	data3.append(spa_data['results'][2]['forecast'][k]['T']) 
	time3.append(k)
	xas1.append(spa_data['results'][2]['forecast'][k]['ftime'])
#print(data3)
#print(time3)
y_min = min(min([list(map(int, data1)),list(map(int, data2)),list(map(int, data3))]))
y_max = max(max([list(map(int, data1)),list(map(int, data2)),list(map(int, data3))]))

plt.plot(time1,data1,'r-',label=spa_data['results'][0]['name'])
plt.plot(time2,data2,'b-',label=spa_data['results'][1]['name'])
plt.plot(time3,data3,'g-',label=spa_data['results'][2]['name'])
plt.xlim(0, 24)
plt.ylim(y_min-1,y_max+1)
plt.ylabel('Hitastig')
plt.xlabel('Spa nr.')
plt.title('test')
plt.grid('on')
plt.xticks(time1, xas1, rotation=45, fontsize=7) 
plt.margins(1)
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,ncol=2, mode="expand", borderaxespad=0.)
plt.show()

#for j in range(0,3):
#	print('Stadsetning:',spa_data['results'][j]['name'])
#	for k in range(0,5):
#		print('Tími:',spa_data['results'][j]['forecast'][k]['ftime'])
#		print('Vedur',spa_data['results'][j]['forecast'][j]['W'],'-','Hitastig:',spa_data['results'][j]['forecast'][k]['T'])
#print(spa_data.keys())
#print(spa_data['results'])
#print(spa_data['results'][0]['name'])
#print(spa_data['results'][0]['forecast'][0])
#print(spa_data['results'][0]['forecast'][0]['D'])
#print(spa_data['results'][0]['forecast'][0]['T'])
#print(spa_data['results'][0]['forecast'][0]['TD'])
#print(spa_data['results'][0]['forecast'][0]['W'])
#print(spa_data['results'][0]['forecast'][0]['N'])
#print(spa_data['results'][0]['forecast'][0]['R'])
#print(spa_data['results'][0]['forecast'][0]['F'])
#print(spa_data['results'][0]['forecast'][0]['ftime'])
#print(type(spa_data['results'][0]['forecast'][0]['ftime']))