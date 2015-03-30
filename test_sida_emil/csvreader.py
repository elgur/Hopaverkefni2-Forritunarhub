import csv

def lesaskra(skra):
	with open(skra) as csvfid:
		#dialect = csv.Sniffer().sniff(csvfid.read(1024))
		a = csv.reader(csvfid,delimiter=',')
		return {row[0]:row[1:] for row in a}