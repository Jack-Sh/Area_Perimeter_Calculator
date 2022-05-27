# functions


# Checks that the response is in the given list
def choice_checker(question, valid_list, error, ):

    # begin the loop
    valid = False
    while not valid:

        # Ask user for choice (and put in lowercase)
        response = input(question).lower()

        # iterates through list and if response is an item
        # in the list (or the first letter of an item), the
        # full item name is returned

        for item in valid_list:
            if response == item[0] or response == item:
                return item

        else:
            print(error)


# main routine

# setup list
valid_shapes = ["square", "rectangle", "circle", "triangle"]

# begin loop
for item in range(0,4):

    # get shape and check that it's valid
    print()
    what_shape = choice_checker("Shape? ", valid_shapes, "Please enter a valid shape\n")
    print()

    if what_shape == "square":
        print("-- Square --")
        dimension_1 = int(input("Enter a side: "))
    elif what_shape == "rectangle":
        print("-- Rectangle --")
        dimension_1 = int(input("Enter the base length: "))
        dimension_2 = int(input("Enter the height length: "))
    elif what_shape == "circle":
        print("-- Circle --")
        dimension_1 = int(input("Enter the radius: "))
    else:
        print("-- Triangle --")
        dimension_1 = int(input("Enter the base length: "))
        dimension_2 = int(input("Enter the height length: "))
        dimension_3 = int(input("Enter the side 2 length: "))
        dimension_4 = int(input("Enter the side 3 length: "))
