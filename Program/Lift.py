def lift():
    max_weight = int(1000)
    max_people = int(14)
    weight = int(input("Weight: "))
    number_of_people = int(input("Number of people: "))
    if weight > max_weight:
        print("Overweight. Maximum is 1000kg. Your weight is",weight)
    elif weight < max_weight:
        if number_of_people > max_people:
            print("Too crowded. Maximum capacity is 14 people. The amount of people here is",number_of_people)
    if weight < max_weight and number_of_people < max_people :
        floor = [1,2,3,4,5,6]
        print ("Floors: ",floor)
        which_floor = int(input("Which floor do you want to go?"))
        if which_floor>0 and which_floor<7 :
            print ("You have arrived at floor",(which_floor))
        else :
            print ("Non existing floor")
