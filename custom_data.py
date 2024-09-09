import json
import time
import datetime
import random
from flask import Flask, jsonify, request
import os.path

path="C:/Users/angel/OneDrive/GitHub/budget_planner/client/components/expenses"
completeName = os.path.join(path, "data.json") 




descriptions=["PIPERORIZA","HELLENIC TRAIN","Pastards","Pet City","SYMFERI","HONDOS CENTER","Fitness Mall","Sinion","SEPHORA","Italian","Mono Bar","STEAM"
			  "ODEON CINEMAS","Netflix","EVPSKROUTZ","COSMOTE AVT TELCO MPAY","MARKET IN CHIOS M415","COFFEE LAB",
			  "MY MARKET 758 XIOS","BLENTER","SHOZO","COFFEEBERRY","MAMOUNAS","TO MAVRO PROVATO STOA",
			  "AMANDIER  SIA GP","LIDL","INTERSPORT","COSMOS SPORT","PLASIO","EVPFAGI","APPLECOMBILL","ZOOFILIA",
			  "ΕΝΤΟΛΗ/ ΕΜΒΑΣΜΑ ΣΕ ΑΛΛΗ ΤΡΑΠΕΖΑ","GERMANOS","VICKO","ZARA"
			  ]



format_string = '%Y-%m-%d %H:%M:%S'


# Data to be written
i=0
accounting_balance=531.55
while (True) :
	now = datetime.datetime.now()
	price= random.randint(2,15)
	accounting_balance= accounting_balance-price
	dictionary = {
		"user_id":'66a927542493534018076593',
		"transaction_id":random.randint(1000,2000),
		"date": now.strftime("%a, %d %b"),
		"time":now.strftime("%H:%M"),
		"name":random.choice(descriptions),
		"price":price,
		"accounting_balance":accounting_balance

	}
	print(now.strftime(" %a, %d %b %H:%M"))
	i+=1
	def write_json(new_data,filename= completeName):
		with open(completeName,'r+') as file:
			file_data = json.load(file)
			# Join new_data with file_data inside emp_details
			file_data["transactions"].append(new_data)
			# Sets file's current position at offset.
			file.seek(0)
			# convert back to json.
			json.dump(file_data, file, indent = 4)
		return print("done")
	write_json(dictionary)
	time.sleep(10)


