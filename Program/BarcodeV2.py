def barcode2():
    items = ["Apple", "Orange", "Banana", "Grape", "Watermelon", "Pineapple", "Durian", "Melon", "Kiwi", "Pear"]
    prices = [1500, 1440, 1330, 1155, 1510, 1610, 2000, 3000, 500, 1900]
    hint = ["Apple = 3210456789", "Orange = 2301547698", "Banana = 5231689192", "Grape = 4341798273", "Watermelon = 3451875364", "Pineapple = 2561964455", "Durian = 1671033546", "Melon = 1030458192", "Kiwi = 8511568193", "Pear = 5711391284"]
    n = int(input("How many items are being bought?"))
    legendcmd = str(input("Do you need the legend? (Yes/No) ")).title().strip()
    message = "\nTotal:" + " " + "RP"
    message1 = "\nPrice Per Kg: "+ "RP"
    message2 = "\nFinal Total:" + " " + "RP"
    amount = "Amount: "
    total = []
    if "Yes" in legendcmd:
            print(hint[:])
            for i in range(n):
                x = int(input('Insert Barcode:'))
                if x == 3210456789:
                    f = int(input(amount))
                    fin0 = prices[0] * f
                    sfin0 = str(fin0)
                    total.append(sfin0)
                    print(items[0]+ ":", f, message, fin0, message1, prices[0])
                if x == 2301547698:
                    f = int(input(amount))
                    fin1 = prices[1] * f
                    sfin1 = str(fin1)
                    total.append(sfin1)
                    print(items[1]+ ":", f, message, fin1, message1, prices[1])
                if x == 5231689192:
                    f = int(input(amount))
                    fin2 = prices[2] * f
                    sfin2 = str(fin2)
                    total.append(sfin2)
                    print(items[2]+ ":", f, message, fin2, message1, prices[2])
                if x == 4341798273:
                    f = int(input(amount))
                    fin3 = prices[3] * f
                    sfin3 = str(fin3)
                    total.append(sfin3)
                    print(items[3]+ ":", f, message, fin3, message1, prices[3])
                if x == 3451875364:
                    f = int(input(amount))
                    fin4 = prices[4] * f
                    sfin4 = str(fin4)
                    total.append(sfin4)
                    print(items[4]+ ":", f, message, fin4, message1, prices[4])
                if x == 2561964455:
                    f = int(input(amount))
                    fin5 = prices[5] * f
                    sfin5 = str(fin5)
                    total.append(sfin5)
                    print(items[5]+ ":", f, message, fin5, message1, prices[5])
                if x == 1671033546:
                    f = int(input(amount))
                    fin6 = prices[6] * f
                    sfin6 = str(fin6)
                    total.append(sfin6)
                    print(items[6]+ ":", f, message, fin6, message1, prices[6])
                if x == 1030458192:
                    f = int(input(amount))
                    fin7 = prices[7] * f
                    sfin7 = str(fin7)
                    total.append(sfin7)
                    print(items[7]+ ":", f, message, fin7, message1, prices[7])
                if x == 8511568193:
                    f = int(input(amount))
                    fin8 = prices[8] * f
                    sfin8 = str(fin8)
                    total.append(sfin8)
                    print(items[8]+ ":", f, message, fin8, message1, prices[8])
                if x == 5711391284:
                    f = int(input(amount))
                    fin9 = prices[9] * f
                    sfin9 = str(fin9)
                    total.append(sfin9)
                    print(items[9]+ ":", f, message, fin9, message1, prices[9])
            final = [int(i) for i in total]
            print(message2, sum(final))
    else:
        for i in range(n):
            x = int(input('Insert Barcode:'))
            if x == 3210456789:
                f = int(input(amount))
                fin0 = prices[0] * f
                sfin0 = str(fin0)
                total.append(sfin0)
                print(items[0]+ ":", f, message, fin0, message1, prices[0])
            if x == 2301547698:
                f = int(input(amount))
                fin1 = prices[1] * f
                sfin1 = str(fin1)
                total.append(sfin1)
                print(items[1]+ ":", f, message, fin1, message1, prices[1])
            if x == 5231689192:
                f = int(input(amount))
                fin2 = prices[2] * f
                sfin2 = str(fin2)
                total.append(sfin2)
                print(items[2]+ ":", f, message, fin2, message1, prices[2])
            if x == 4341798273:
                f = int(input(amount))
                fin3 = prices[3] * f
                sfin3 = str(fin3)
                total.append(sfin3)
                print(items[3]+ ":", f, message, fin3, message1, prices[3])
            if x == 3451875364:
                f = int(input(amount))
                fin4 = prices[4] * f
                sfin4 = str(fin4)
                total.append(sfin4)
                print(items[4]+ ":", f, message, fin4, message1, prices[4])
            if x == 2561964455:
                f = int(input(amount))
                fin5 = prices[5] * f
                sfin5 = str(fin5)
                total.append(sfin5)
                print(items[5]+ ":", f, message, fin5, message1, prices[5])
            if x == 1671033546:
                f = int(input(amount))
                fin6 = prices[6] * f
                sfin6 = str(fin6)
                total.append(sfin6)
                print(items[6]+ ":", f, message, fin6, message1, prices[6])
            if x == 1030458192:
                f = int(input(amount))
                fin7 = prices[7] * f
                sfin7 = str(fin7)
                total.append(sfin7)
                print(items[7]+ ":", f, message, fin7, message1, prices[7])
            if x == 8511568193:
                f = int(input(amount))
                fin8 = prices[8] * f
                sfin8 = str(fin8)
                total.append(sfin8)
                print(items[8]+ ":", f, message, fin8, message1, prices[8])
            if x == 5711391284:
                f = int(input(amount))
                fin9 = prices[9] * f
                sfin9 = str(fin9)
                total.append(sfin9)
                print(items[9]+ ":", f, message, fin9, message1, prices[9])
        final = [int(i) for i in total]
        print(message2, sum(final))

