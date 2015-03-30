from flask import render_template
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
@app.route('/')
@app.route('/index')
def index():
		return render_template('index.html',
								stadi='staði',
								lyklarnir =lyklar)
