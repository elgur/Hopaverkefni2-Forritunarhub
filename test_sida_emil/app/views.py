from flask import render_template, request, jsonify
from app import app
from csvreader import lesaskra
# setja inn í class ?
nofni = lesaskra("dop.csv")
lyklar = list(nofni.keys())
lykl = []
for x in sorted(lyklar):
	lykl.append(x)
lyklar =lykl
## setja inn í class?
stillingar = [ ]

@app.route('/', methods = ['GET','POST'])
@app.route('/index', methods = ['GET','POST'])
def index():
		return render_template('index.html',
								stadi='staði',
								lyklarnir =lyklar)
@app.route('/saekja', methods=['GET','POST'])
def saekja_box():
	stillingar = request.form.getlist("still")
	stodvar = request.form.getlist("stod") 
	print(stillingar)
	print(stodvar)
	return index()
