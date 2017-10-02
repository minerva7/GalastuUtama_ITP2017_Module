def barcode():
    x = int(input('Insert x:'))
    y = int(input('Insert y:'))
    z = int(input('Insert z:'))
    a = int(input('Insert a:'))
    b = int(input('Insert b:'))
    c = int(input('Insert c:'))
    d = int(input('Insert d:'))
    e = int(input('Insert e:'))
    f = int(input('Insert f:'))
    g = int(input('Insert g:'))

    items = ["Apple", "Orange", "Banana", "Grape", "Watermelon", "Pineapple", "Durian"]
    if x == 3 and y == 2 and z == 1 and a == 0 and b == 4 and c == 5 and d == 6 and e == 7 and f == 8 and g == 9:
        print('\n' + items[0] + ': Rp. 2500/kg')
    elif x == 2 and y == 3 and z == 0 and a == 1 and b == 5 and c == 4 and d == 7 and e == 6 and f == 9 and g == 8:
        print('\n' + items[1] + ': Rp. 1500/kg')
    elif x == 5 and y == 2 and z == 3 and a == 1 and b == 6 and c == 8 and d == 9 and e == 1 and f == 8 and g == 2:
        print('\n' + items[2] + ': Rp. 2000/kg')
    elif x == 4 and y == 3 and z == 4 and a == 1 and b == 7 and c == 9 and d == 8 and e == 2 and f == 7 and g == 3:
        print('\n' + items[3] + ': Rp. 1500/kg')
    elif x == 3 and y == 4 and z == 5 and a == 1 and b == 8 and c == 7 and d == 5 and e == 3 and f == 6 and g == 4:
        print('\n' + items[4] + ': Rp. 1500/kg')
    elif x == 2 and y == 5 and z == 6 and a == 1 and b == 9 and c == 6 and d == 4 and e == 4 and f == 5 and g == 5:
        print('\n' + items[5] + ': Rp. 1500/kg')
    elif x == 1 and y == 6 and z == 7 and a == 1 and b == 0 and c == 3 and d == 3 and e == 5 and f == 4 and g == 6:
        print('\n' + items[6] + ': Rp. 1500/kg')
    else:
        print('\nBarcode not found.' + '\nSorry. The food is not available.')
##Barcode for Apple        : 3210456789##
##Barcode for Orange       : 2301547698##
##Barcode for Banana       : 5231689192##
##Barcode for Grape        : 4341798273##
##Barcode for Watermeon    : 3451875364##
##Barcode for Pineapple    : 2561964455##
##Barcode for Durian       : 1671033546##

