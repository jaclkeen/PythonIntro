my_family = { 'sister': { 'name': 'Krista', 'age': 42 }, 
            'mother': { 'name': 'Cathie', 'age': 70 } }

for fam in my_family:
    print "This is my " + fam + " " + my_family[fam]['name'] + " and she is " + str(my_family[fam]['age'])