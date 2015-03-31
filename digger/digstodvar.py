import urllib.request, json
import time

class digg:
	def forecast(tolur):
		
		for i in tolur:
			grunn_uppl = 'http://apis.is/weather/forecasts/is?stations='
			uppl_breytt = grunn_uppl+str(i)
			time.sleep(0.5)
			try:
				u_response = urllib.request.urlopen(uppl_breytt)
			except:
				pass
			else:
				uppl_data = json.loads(u_response.read().decode('utf8'))
				stod = uppl_data['results'][0]
				print(stod['name'],stod['id'])
			finally:
				pass
	def observation():
		output = []
		l = 1
		for k in range(1,12):
			grunn_uppl = 'http://apis.is/weather/observations/is?stations='
			for i in range(l,l+999):
				if i == l:
					grunn_uppl = grunn_uppl+str(i)
				else:
					grunn_uppl = grunn_uppl+','+str(i)
			try:
				u_response = urllib.request.urlopen(grunn_uppl)
				uppl_data = json.loads(u_response.read().decode('utf8'))
			except:
				pass
			else:
				for stod in uppl_data['results']:
					print(stod['name'],stod['id'])
					output.append(stod['id'])
			finally:
				l = l + 999
		return output
digg.forecast(digg.observation())