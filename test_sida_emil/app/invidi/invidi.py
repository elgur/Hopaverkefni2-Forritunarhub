import urllib.request, json
import csv
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure
from matplotlib.dates import DateFormatter
import numpy
import io
import base64
from flask import send_file

class gogn:
	def __init__():
		pass
	def saekja(stodvanumer):
		'''
			Þetta fall tekur inn stöðvarnúmer og 
			skilar tveimur dictionary frá apis
			á forminu: 
		'''
		grunn_uppl = 'http://apis.is/weather/observations/is?stations='
		uppl_url = grunn_uppl+str(stodvanumer)
		grunn_spa = 'http://apis.is/weather/forecasts/is?stations='
		spa_url = grunn_spa+str(stodvanumer)
		u_response = urllib.request.urlopen(uppl_url)
		s_response = urllib.request.urlopen(spa_url)
		uppl_data = json.loads(u_response.read().decode('utf8'))
		spa_data = json.loads(s_response.read().decode('utf8'))
		return uppl_data,spa_data
	def csvDict(skra):
		'''
			þetta fall tekur inn csv skrá 
			og skila dictionary
		'''
		with open(skra) as csvfid:
			a = csv.reader(csvfid,delimiter=',')
			return {row[0]:row[1:] for row in a}
	def stafrofsrod(ordabok):
		'''
			Þetta fall breytir dictionry lyklum í
			lista sem er í stafrófsröð
		'''
		lykl = []
		lyklar = list(ordabok.keys())
		for x in sorted(lyklar):
			lykl.append(x)
		return lykl
	def textabrot(spa_data):
		'''
			Þetta fall breytir upplýsingum og kemur þeim á formið
			Dagsetning:tímasetnig:gögn
		'''
		vedur_timasetningar = {}
		for i in spa_data['results'][0]['forecast']:
			i_tmp =dict(i) # gerum afrit af dict. svo orginal uppfærist ekki.
			i_tmp.pop('ftime',None) # fjarlægum tíma.
			if i['ftime'][0:10] not in vedur_timasetningar.keys():
				vedur_timasetningar[i['ftime'][0:10]] = [{i['ftime'][-8:]:i_tmp}]
			else:
				vedur_timasetningar[i['ftime'][0:10]][0].update({i['ftime'][-8:]:i_tmp})
		return vedur_timasetningar

class mynd:
	def __init__():
		pass
	def prentamynd(gogn,hvad,myndin):
		'''

		Þetta fall plotar valinn gögn og skilar þeim inn
		í "myndin" 

		'''
		plt.clf()
		ygogn = []
		xgogn = []
		for i in gogn['results'][0]['forecast']:
			ygogn.append(i[hvad])
			xgogn.append(i['ftime'])
		y_min = min(min([map(float, ygogn)]))
		y_max = max(max([map(float, ygogn)]))
		plt.plot(range(0,len(xgogn)),ygogn,'r-')#,label=gogn['results'][0]['name'])
		plt.xlim(0, len(xgogn))
		plt.ylim(y_min-1,y_max+1)
		#plt.ylabel(hvad)
		plt.xlabel('Spa nr.')
		plt.grid('on')
		plt.xticks(range(0,len(xgogn)), xgogn, rotation=45, fontsize=7) 
		plt.margins(1)
		plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,ncol=2, mode="expand", borderaxespad=0.)
		plt.savefig(myndin,format ='png')
		