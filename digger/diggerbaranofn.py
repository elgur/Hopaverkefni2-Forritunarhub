import urllib.request, json
import csv
l = 1
with open('diggeroutputbaranofn.csv','w',newline='') as csvfile:
	skrifari = csv.writer(csvfile) 
	for k in range(1,12):
		grunn_uppl = 'http://apis.is/weather/observations/is?stations='
		for i in range(l,l+999):
			if i == l:
				grunn_uppl = grunn_uppl+str(i)
			else:
				grunn_uppl = grunn_uppl+','+str(i)
		#		print(grunn_uppl)
		try:
			u_response = urllib.request.urlopen(grunn_uppl)
			uppl_data = json.loads(u_response.read().decode('utf8'))
		except:
			pass
		else:
			for stod in uppl_data['results']:
				print(stod['name'],stod['id'])
				output = [str(stod['name'])]
				#print(output)
				skrifari.writerow(output)
		finally:
			l = l + 999
			print(l)

 
#print(grunn_uppl)
#print(uppl_data)






# uppl_data = json.loads(u_response.read().decode('utf8'))
# spa_data = json.loads(s_response.read().decode('utf8'))
# print(uppl_data['results'][0]['name'],":", stodvanumer)



#f = open('diggeroutput.txt','W')
#f.write(str(uppl_data['results'[0]['name'],stodvanumer))