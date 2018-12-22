from django.shortcuts import render

def home(request):
	import requests
	import json

	#Grabing crypto price
	price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,XRP,ETH,BCH,EOS,LTC,XLM,ADA,USDT,MIOT&tsyms=USD")
	price = json.loads(price_request.content)

	# Grabing crypto&Blockchain news
	api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
	api = json.loads(api_request.content)
	return render(request,'home.html',{'api':api, 'price' :price})

def prices(request):
	if request.method == 'POST':
		quote = request.POST['quote']
		return render(request, 'prices.html', {'quote':quote})

	else:
		return render(request, 'prices.html',{})
