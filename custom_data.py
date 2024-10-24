import time
import datetime
import random
import requests





descriptions=[["PIPERORIZA","Eating Out"],["HELLENIC TRAIN","Transportation"],["Pastards","Eating Out"],["Pet City","Pet Care"],["SYMFERI","Household"],
			  ["HONDOS CENTER","Personal Care"],["Fitness Mall","Personal Care"],["Sinion","Personal Care"],["SEPHORA","Personal Care"],
			  ["Mono Bar","Night Out"],["STEAM","Entertainment"],["ODEON CINEMAS","Entertainment"],["Netflix","Subsriptions"],
			  ["EVPSKROUTZ","Shopping"],["COSMOTE AVT TELCO MPAY","Bills"],["MARKET IN CHIOS M415","Groceries"],
			  ["COFFEE LAB","Groceries"],["BLENTER","Eating Out"],["SHOZO","Eating Out"],["COFFEEBERRY","Eating Out"],
			  ["MAMOUNAS","Eating Out"],["TO MAVRO PROVATO STOA","Eating Out"],["AMANDIER SIA GP","Groceries"],["LIDL","Supermarket"],
			  ["INTERSPORT","Shopping"],["COSMOS SPORT","Shopping"],["PLASIO","Shopping"],["EVPFAGI","Food Delivery"],["Wolt","Food Delivery"],
			  ["APPLECOMBILL","Bills"],["ZOOFILIA","Pet Care"],["ΕΝΤΟΛΗ/ ΕΜΒΑΣΜΑ ΣΕ ΑΛΛΗ ΤΡΑΠΕΖΑ","Personal loand"],["GERMANOS","Bills"],
			  ["VICKO","Shopping"],["ZARA","Shopping"],["MASOUTIS","Groceries"],["TIGER HELLAS SA","Shopping"],["BOX FOOD APP","Food Delivery"],
			  ["AB PATRA 2 23","Groceries"],["NESPRESSO HELLAS SA","Groceries"],["PayPal Europe_HQHC","Credit Card"],["Revolut0689","Credit Card"]]




format_string = '%Y-%m-%d %H:%M:%S'


def generateTransaction(accounting_balance):
	now = datetime.datetime.now()
	price= random.randint(2,15)
	randomTransaction=random.choice(descriptions)
	# global accounting_balance
	accounting_balance= accounting_balance-price
	newTransaction = {
		"user_id":'66a927542493534018076593',
		"transaction_id":random.randint(1000,20000000),
		"date": now.strftime("%d/%m/%Y"),
		"time":now.strftime("%H:%M"),
		"description":randomTransaction[0],
		"price":-price,
		"category":randomTransaction[1],
		"accounting_balance":accounting_balance

	}
	return newTransaction



def sendTransaction(newTransaction):
	try:
		response = requests.post("https://budget-planner-backend-mcuw.onrender.com/api/receive-transaction", json=newTransaction)
		if response.status_code == 200:
			print("Transaction sent successfully!")
		else:
			print(f"Failed to send transaction. Status code: {response.status_code}")
	except requests.exceptions.RequestException as e: print(e)




while True:
	try:
		user_id={"id":"66a927542493534018076593"}
		accounting_balance=requests.post("https://budget-planner-backend-mcuw.onrender.com/api/fetch-data",data={"id":"66a927542493534018076593"}).json()
		print(accounting_balance)
		transaction = generateTransaction(accounting_balance)
		print(transaction)
		sendTransaction(transaction)
		time.sleep(100)
		# time.sleep(43200)
	except requests.exceptions.RequestException as e: print(e)
