import flask
from flask import render_template,session, request, jsonify, send_file,send_from_directory
from app import app
import urllib
import os
import io
from app.invidi.invidi import gogn, mynd

''' 

Frum stillingar og gögn

'''
nofni = gogn.csvDict("app\invidi\dop.csv")
lyklar =  gogn.stafrofsrod(nofni)
stillingar = []


"""
Hér fyrir neðan er server vefsíðunar keyrður.

"""
@app.route('/', methods = ['GET','POST'])
def index():
	# Þetta fall skilar index() síðu veðurfrétta
	# stillingar eru tómar í byrjun.
		return render_template('index.html',
								lyklarnir =lyklar,
								ordabok = nofni,
								still = stillingar)

							
@app.route('/saekja', methods=['GET','POST'])
def saekja_box():
	'''
	þetta fall sækir upplýsingar er ýtt er á post
	á síðunni. skilar þeim inní session. 
	'''
	stodvar = request.form.getlist('stod')
	uppl_data,spa_data = gogn.saekja(stodvar[0])
	session['spagogn'] = spa_data
	vedur_uppl = uppl_data['results'][0]
	vedur_timasetningar = gogn.textabrot(spa_data)
	return render_template('vedurstod.html',
							lyklarnir =lyklar,
							ordabok = nofni,
							uppl=vedur_uppl,
							still = stillingar),


@app.route('/plothiti.png')
def myndhiti():
	'''
	Myndin er uppi í 5 sekúndur. Eftir það er
	kallað aftur á þetta fall. 
	'''
	spa_data=session['spagogn']
	plotid = io.BytesIO()
	mynd.prentamynd(spa_data,'T',plotid)
	plotid.seek(0)
	return send_file(plotid,
		# Myndin er upp í 5 sec.
					cache_timeout = 5,
					mimetype='image/png',
					attachment_filename="plothiti.png",
					as_attachment=True)

@app.route('/plotregn.png')
def myndregn():
	'''
	Myndin er uppi í 5 sekúndur. Eftir það er
	kallað aftur á þetta fall. 
	'''
	spa_data=session['spagogn']
	plotid = io.BytesIO()
	mynd.prentamynd(spa_data,'R',plotid)
	plotid.seek(0)
	return send_file(plotid,
		# Myndin er upp í 5 sec.
					cache_timeout = 8,
					mimetype='image/png',
					attachment_filename="plotregn.png",
					as_attachment=True)

app.secret_key = os.urandom(24)
