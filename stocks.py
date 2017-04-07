#Create a purchase history report that computes the full purchase price (shares times dollars) 
#for each block of stock and uses the stockDict to look up the full company name.

#ticker symbols and company names
stockDict = { 
'GM':'General Motors',
'CAT':'Caterpillar', 
'EK':"Eastman Kodak",
'AFL':"Aflac",
'AMZN':"Amazon",
'GOOGL':"Google"
}


#ticker symbols, number of shares, dates and price.
purchases = [ 
( 'CAT', 100, '1-apr-1999', 24 ),
( 'GM', 100, '10-sep-2001', 48 ),
( 'CAT', 100, '1-apr-1999', 24 ),
( 'GM', 200, '1-jul-1998', 56 ),
( 'AFL', 100, '1-jul-1998', 65 ),
( 'AMZN', 100, '1-jul-1998', 23 ),
( 'AMZN', 300, '1-jul-1998', 16 ),
( 'GOOGL', 400, '1-jul-1998', 87 )
]

# for purchase in purchases:
# 	ticker = purchase[0]

# 	full_company_name = stockDict[ticker]

# 	number_of_shares = purchase[1]
# 	purchase_price = purchase[3]
# 	full_purchase_price = number_of_shares * purchase_price

# 	#print("%.2f" % full_purchase_price)
# 	print("I purchased {0} stock for ${1}".format(full_company_name, full_purchase_price))


#Create a second purchase summary that which accumulates total investment by ticker symbol.
#creating a dict where the key is the ticker and the value is the list of blocks purchased.
#The program makes one pass through the data to create the dict. 
#A pass through the dict can then create a report showing each ticker symbol and all blocks of stock.

portfolio = dict()
for purchase in purchases:
	ticker = purchase[0]

	full_company_name = stockDict[ticker]
	number_of_shares = purchase[1]
	purchase_price = purchase[3]
	full_purchase_price = number_of_shares * purchase_price

	try:
		portfolio[ticker].append(purchase)	#append the purchase to the ticker list
	except KeyError:
		portfolio[ticker] = list()			#if key doesn't exist yet, create it
		portfolio[ticker].append(purchase)

print("I purchased {} stock for ${}".format(full_company_name, full_purchase_price))

for ticker,purchases in portfolio.items():
	print("----- {} ------".format(ticker))
	total_stock_value = 0
	for purchase in purchases:
		total_stock_value += purchase[1] * purchase[3]
		print("   {}".format(purchase))
	print("Total stock: ${}\n\n".format(total_stock_value))

print(portfolio)