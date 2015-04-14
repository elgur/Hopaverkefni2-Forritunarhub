import flask
from flask import render_template,session, request, jsonify, send_file
from app import app
from invidi import gogn, mynd
import urllib
import base64
import io
''' 

Frum stillingar og gögn

'''
nofni = gogn.csvDict("dop.csv")
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
	#þetta fall sækir upplýsinfar er ýtt er á post
	# á síðunni
	# sækjum upplýsingar frá templetinu
	stillingar = request.form.getlist('still')
	stodvar = request.form.getlist('stod')
	uppl_data,spa_data = gogn.saekja(stodvar[0])
	session['spagogn'] = spa_data
	session['stilur'] = stillingar
	vedur_uppl = uppl_data['results'][0]

	return render_template('index.html',
							lyklarnir =lyklar,
							ordabok = nofni,
							uppl=vedur_uppl,
							still = stillingar),


@app.route('/plotid2.png')
def myndin():
	spa_data=session['spagogn']
	stillingar=session['stilur']
	print(spa_data)
	print(stillingar)
	plotid = io.BytesIO()
	mynd.prentamynd(spa_data,stillingar[0],plotid)
	plotid.seek(0)
	return send_file(plotid,
					cache_timeout = 5,
					mimetype='image/png',
					attachment_filename="plotid2.png",
					as_attachment=True)

app.secret_key = 'faædlfkaælkefæalmfdsg'
