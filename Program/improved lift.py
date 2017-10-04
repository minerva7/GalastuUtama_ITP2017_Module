def lift():
    max_weight = int(1000)
    people1 = int(input('weight of person no 1: '))
    people2 = int(input('weight of person no 2: '))
    people3 = int(input('weight of person no 3: '))
    people4 = int(input('weight of person no 4: '))
    people5 = int(input('weight of person no 5: '))
    people6 = int(input('weight of person no 6: '))
    people7 = int(input('weight of person no 7: '))
    people8 = int(input('weight of person no 8: '))
    people9 = int(input('weight of person no 9: '))
    people10 = int(input('weight of person no 10: '))
    people11 = int(input('weight of person no 11: '))
    people12 = int(input('weight of person no 12: '))
    people13 = int(input('weight of person no 13: '))
    people14 = int(input('weight of person no 14: '))
    print ('If there is no person no 15, type (0)')
    people15 = (input('weight of person no 15: '))
    if people15 != '0':
        print("Too crowded. Maximum capacity is 14 people.")
    weight = (people1+people2+people3+people4+people5+people6+people7+people8+people9+people10+people11+people12+people13+people14)
    if weight > max_weight:
        print("Overweight. Maximum is 1000kg. Your weight is",weight)
    elif weight < max_weight:
        if weight < max_weight:
            floor = [1,2,3,4,5,6]
            print ("Floors: ",floor)
            which_floor = int(input("Which floor do you want to go?"))
            while (which_floor < 7 and which_floor > 0):
                print ("You have arrived at floor",(which_floor))
                which_floor = int(input("Which floor do you want to go?"))
            else:
                print ("Non existing floor")
                which_floor = int(input("Which floor do you want to go?"))
lift()
