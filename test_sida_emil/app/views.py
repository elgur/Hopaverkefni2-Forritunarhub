from flask import render_template, request, jsonify
from app import app
import csv
# setja inn í class ?
#
# setja í inviði
# 
def csvDict(skra):
	with open(skra) as csvfid:
		a = csv.reader(csvfid,delimiter=',')
		return {row[0]:row[1:] for row in a}
#
# setja í inviði
#
nofni = csvDict("dop.csv")
lyklar = list(nofni.keys())
lykl = []
for x in sorted(lyklar):
	lykl.append(x)
## setja inn í class?
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
								lyklarnir =lykl,
								ordabok = nofni,
								still = stillingar)
@app.route('/saekja', methods=['GET','POST'])
def saekja_box():
	#þetta fall sækir upplýsinfar er ýtt er á post
	# á síðunni
	stillingar = request.form.getlist('still')
	stodvar = request.form.getlist('stod') 
	print(stillingar)
	print(stodvar)
	return render_template('index.html',
								stadi='staði',
								lyklarnir =lykl,
								ordabok = nofni,
								still = stillingar)