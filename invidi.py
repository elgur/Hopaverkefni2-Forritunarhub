import urllib.request, json
class gogn:
	def _init_():
		pass
	def saekja(stodvanumer,hvad):
		grunn_uppl = 'http://apis.is/weather/observations/is?stations='
		uppl_url = grunn_uppl+str(stodvanumer)
		grunn_spa = 'http://apis.is/weather/forecasts/is?stations='
		spa_url = grunn_spa+str(stodvanumer)
		u_response = urllib.request.urlopen(uppl_url)
		s_response = urllib.request.urlopen(spa_url)
		uppl_data = json.loads(u_response.read().decode('utf8'))
		spa_data = json.loads(s_response.read().decode('utf8'))
		if hvad == spa:
			return spa_data
		elif hvad == uppl:
			return uppl_data
		elif hvad == baedi:
			return uppl_data,spa_data
	def timi_hitasti(spa_data):
		timi = []
		hitastig = []
		for i in spa_data['results'][0]['forecast']:
			timi.append(i['ftime'])
			hitastig.append(i['T'])
		return timi,hitastig
print(gogn.timi_hitasti(gogn.saekja(1,spa)))


