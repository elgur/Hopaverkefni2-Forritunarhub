from flask import render_template, request, jsonify
from app import app
from invidi import gogn
import Vedurstod
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
@app.route('/index', methods = ['GET','POST'])
def index():
	# Þetta fall skilar index() síðu veðurfrétta
	# stillingar eru tómar í byrjun.
		return render_template('index.html',
								stadi='staði',
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
	vedur_uppl = uppl_data['results'][0]
	## staðsetning debug prentunar
	# hér þarf að taka # í burtu
	stod1 = Vedurstod.stod(int(stodvar[0]))
	stod1_mynd = Vedurstod.PrentaMynd(stod1,stillingar[0])
	return render_template('index.html',
								stadi='staði',
								lyklarnir =lyklar,
								ordabok = nofni,
								still = stillingar,
								uppl=vedur_uppl)
@app.route('/saekja', methods=['GET','POST'])
def uppfaera_mynd():
	return render_template('mynd.html')