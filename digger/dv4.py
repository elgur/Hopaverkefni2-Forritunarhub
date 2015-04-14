import urllib.request, json
import time
import csv
import requests
class digg:
	def forecast(tolur):
		with open('dv4.csv','w',newline='') as csvfile:
			skrifari = csv.writer(csvfile) 
			grunn_uppl = 'http://apis.is/weather/forecasts/is?stations='
			numer = []
			for i in tolur:
				time.sleep(0.5)
				uppl_breytt = grunn_uppl+str(i)
				req = requests.head(uppl_breytt)
				if req.status_code == 200:
					numer.append(i)
			grunn_uppl = 'http://apis.is/weather/observations/is?stations='
			sidu_uppl = grunn_uppl+str(numer[0])
			for i in numer[1:]:
				sidu_uppl = sidu_uppl+','+str(i)
			u_response = urllib.request.urlopen(sidu_uppl)
			uppl_data = json.loads(u_response.read().decode('utf8'))
			for stod in uppl_data['results']:
				print(stod['name'],stod['id'])
				output =[stod['name'],stod['id']]
				skrifari.writerow(output)
			

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