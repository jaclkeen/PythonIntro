stockDict = { 'GM': 'General Motors',
        'CAT':'Caterpillar', 'EK':"Eastman Kodak"}

purchases = [ ( 'GE', 100, '10-sep-2001', 48 ),
        ( 'CAT', 100, '1-apr-1999', 24 ),
        ( 'GE', 200, '1-jul-1998', 56 ) ]

newPurchases = dict()

for p in purchases:
    stockName = stockDict.get(p[0])
    print "Full Purchase Price: ", stockName, p[1] * p[3]

    if newPurchases.has_key(p[0]):
        newPurchases[p[0]] += p[1]*p[3]      
    else:
        newPurchases[p[0]] = p[1]*p[3]

print "Combined Purchases: ", newPurchases