import os
import unittest
from app import app
import invidi


class FlaskTest(unittest.TestCase):

	'''
	Prófum uppsetningu
	'''
	def setUp(self):
		app.config['TESTING'] = True
		self.app = app.test_client()
		db.create_all()
	'''
	prófum niðurtöku
	'''
	def tearDown(self):
		db.session.remove()
		db.drop_all()
	'''
	prófum hvort csv-file er tekinn inn
	'''
	def test_csv(self):
		sott_tmp = gogn.csvDict("dop.csv")
		sott_tmp = gogn.stafrofsrod(sott_tmp)
		sott = sott[0]
		rett = 'Akureyri'
		assert sott == rett
	'''
	prófum hvort upplýsingar af apis.is eru teknar inn
	'''
	def saekjauppls(self):
		uppl_data,spa_data = gogn.saekja(1)
		grunn_uppl = 'http://apis.is/weather/observations/is?stations=1'
		grunn_spa = 'http://apis.is/weather/forecasts/is?stations=1'
		u_response = urllib.request.urlopen(uppl_url)
		s_response = urllib.request.urlopen(spa_url)
		uppl_data_test = json.loads(u_response.read().decode('utf8'))
		spa_data_test = json.loads(s_response.read().decode('utf8'))
		assert uppl_data == uppl_data_test and spa_data == spa_data_test

if __name__ == '__main__':
	unittest.main()