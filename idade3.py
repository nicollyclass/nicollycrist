id = float(input('digite sua idade'))

if id <= 13:
    print(id, 'criança')
    
elif id <= 13 and 17:
    print(id, 'adolecente')
    
elif id >= 18 and id <= 59:
    print(id, 'adulto')
    
else:
    id >= 60
    print(id, 'idoso')
