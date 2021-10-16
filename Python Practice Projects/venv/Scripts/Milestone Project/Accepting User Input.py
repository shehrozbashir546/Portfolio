#result = input("Enter an Number")
#int_result = int(result)
#print(type(int_result))


def user_choice():

    #Variables
    choice = 'Wrong'
    acceptable_range = range (0,10)
    within_range = False

    while choice.isdigit() == False or within_range==False:
        choice = input("Please enter a number from 0 to 10: ")
        #Digit Check
        if choice.isdigit() == False:
            print("Thats not a digit")
        #Range Check
        if choice.isdigit() == True:
            if int(choice) in acceptable_range:
                within_range = True
                print("Mission Accomplished")
            else:
                within_range = False
                print('You are out the acceptable range')
                break
    return int(choice)

user_choice()
