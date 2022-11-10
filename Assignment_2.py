# This program is for Arnolds Amazing Eats, a restaurant that needs a new ordering software.


# This dictionary is to display the name and prices of the items on the menu.

arnoldsAmazingMenu = {
    1 : 'Hamburger Combo: $22.45',
    2 : 'Personal Pizza:  $19.50',
    3 : 'Calzone:         $15.50',
    4 : 'Chicken Tenders: $12.99',
    5 : 'Chicken Wrap:    $11.99',
    6 : 'Quit'
}

# The below dictionary exists for display purposes in the menu

arnoldsAmazingPricelessMenu = {
    1 : 'Hamburger Combo:  ',
    2 : 'Personal Pizza:   ',
    3 : 'Calzone:          ',
    4 : 'Chicken Tenders:  ',
    5 : 'Chicken Wrap:     ',
}

# The below funtions are the main bod of the program, where all of the math operations take place. the math they are responsible for
# relate directly to their titles and variable names.

def printDictionary(dict):

    for option in dict:

        print(option, dict[option])

def menuConfirmation(menuOption, itemAmount):

            confirm = arnoldsAmazingMenu[menuOption]

            print('you have ordered ', itemAmount, ' units of ', confirm)

def finalMenuOption(menuOption):

    final = arnoldsAmazingMenu[menuOption]

    return final

def finalMenuOutput(menuOption):

    finalTwo = arnoldsAmazingPricelessMenu[menuOption]

    return finalTwo

def selectionPrice(menuOption, itemAmount):

    if menuOption == 1:

        return round((22.45)*(itemAmount), 2)

    elif menuOption == 2:

        return round((19.50)*(itemAmount), 2)

    elif menuOption == 3:

        return round((15.50)*(itemAmount), 2)

    elif menuOption == 4:

        return round((12.99)*(itemAmount), 2)

    elif menuOption == 5:

        return round((11.99)*(itemAmount), 2)

    elif menuOption == 6:

        exit()

def discountAmount(grossTotal):

    if grossTotal <= 100:

        disOne = round((grossTotal*0.05), 2)

        return disOne

    elif grossTotal > 100 and grossTotal <= 500:

        disTwo = round((grossTotal*0.1), 2)

        return disTwo

    elif grossTotal > 500:

        disThree = round((grossTotal*0.15), 2)

        return disThree 

def studentDiscountAmount(isStudent, grossTotal):

    if isStudent == 'y' or isStudent == 'Y':

        return round((grossTotal*0.1), 2)

    else:

        return 0

def subTotalAmount(isStudent: str, grossTotal: float, discount: float):

    if isStudent == 'y' or isStudent == 'Y':

        student = round((grossTotal*0.1), 2)

        return (grossTotal - discount - student)

    else:

        return round((grossTotal - discount), 2)

def taxEffect(subTotal: float):

    return round(((subTotal)*(0.13)), 2)

def deliveryEffect(isDelivery, subTotal):

    if isDelivery == 'y' or isDelivery == 'Y':

        if subTotal < 30:

            return 5

        else:

            return 0

    else:

        return 0

def tipEffect(tipAmount):

    if tipAmount == 1:

        return round((subTotal*0.1), 2)

    elif tipAmount == 2:

        return round((subTotal*0.15), 2)

    elif tipAmount == 3:

        return round((subTotal*0.2), 2)

    elif tipAmount == 4:

        return 0

def totalAmount(subTotal, delivery, tax, tip):

    return round((subTotal + delivery + tax + tip), 2)

# The below questions ask the user for personal information for the delivery.

print('Hello, welcome to Arnolds Amazing Eats\n\nBefore we begin making your delicious meal, we need to know a little about you!\n')

name = input('What is your name?: ')

deliveryAddress = input('Please give us your delivery address [Street Number], [Street Name], [Unit # (if applicable)]: ')

city = input('What city do you live in?: ')

province = input('What province do you live in?: ')

postalCode = input('What is your postal code?: ')

phoneNumber = input('What is your phone number?: ')

specialInstructions = input('Are there any special instructions for this delivery?: ')

print('')

# The below dictionary stores the users personal information.

personalInformation = {
    'Name:                 ' : name,
    'Address:              ' : deliveryAddress,
    'City:                 ' : city,
    'Province:             ' : province,
    'Postal Code:          ' : postalCode,
    'Phone number:         ' : phoneNumber,
    'Special instructions: ' : specialInstructions
}

# The below loop keeps the program functioning

while True:

    printDictionary(arnoldsAmazingMenu)

    menuOption =  input('\nWhat item would you like to order?: ')

    menuOption = int(menuOption)

    # The below loop ensures the user has entered the correct input

    while menuOption < 1 or menuOption > 6:

            menuOption =  input('\n[ERROR] What item would you like to order?: ')

            menuOption = int(menuOption)

    if menuOption == 6:

        exit()

    itemAmount = input('How much of this item would you like?: ')

    # The below loop ensures the user has entered the correct input

    while itemAmount.isnumeric == False:

        itemAmount = input('[ERROR] How much of this item would you like?: ')

    itemAmount = int(itemAmount)

    menuConfirmation(menuOption, itemAmount)

    correctOne = input('Is this correnct? [Y/N]: ')

    # The below loop confims the users order.

    if correctOne == 'y' or correctOne == 'Y':

        isStudent = input('Are you a student? [Y/N]: ')

        isDelivery = input('Is this order for delivery? [Y/N]: ')

        tipAmount = input('How much would you like to tip? [1: 10%, 2: 15%, 3: 20%, 4: 0%]: ')

        tipAmount = int(tipAmount)

        while tipAmount < 1 or tipAmount > 4:

            tipAmount = input('[ERROR] How much would you like to tip? [1: 10%, 2: 15%, 3: 20%, 4: 0%]: ')

            tipAmount = float(tipAmount)

        grossTotal = selectionPrice(menuOption, itemAmount)

        studentDiscount = studentDiscountAmount(isStudent, grossTotal)

        discount = discountAmount(grossTotal)

        subTotal = subTotalAmount(isStudent, grossTotal, discount)

        tax = taxEffect(subTotal)

        delivery = deliveryEffect(isDelivery, subTotal)

        tip = tipEffect(tipAmount)

        total = totalAmount(subTotal, delivery, tax, tip)

        print('You will find your receipt below:\n')

        # The below dictionary is to display and store the receipt information.

        receipt = {

            finalMenuOutput(menuOption) : grossTotal,
            'Discount:         ' : discount,
            'Student Discount: ' : studentDiscount,
            'Sub Total:        ' : subTotal,
            'Tax:              ' : tax,
            'Delivery:         ' : delivery,
            'Tip:              ' : tip,
            'Total:            ' : total
        }

        printDictionary(receipt)

        print('\nYour delivery details are as follows:\n')

        printDictionary(personalInformation)

        break