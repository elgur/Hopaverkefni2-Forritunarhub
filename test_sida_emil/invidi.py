import urllib.request, json
import csv
class gogn:
	def _init_():
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
