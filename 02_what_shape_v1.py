# functions


# Choice checker function, response must be out of a specified valid list
# also works for the first letter of the word
def choice_checker(question, valid_list, error,):

    valid = False
    while not valid:

        # Ask user for choice (and put in lowercase)
        response = input(question).lower()

        # iterates through list and if response is an item
        # in the list (or the first letter of an item), the
        # full item name is returned

        for item in valid_list:
            if response == item[0] or response == item:
                print(item)
                return item

        else:
            print(error)


# main routine

# setup list
valid_shapes = ["square", "rectangle", "circle", "triangle"]

# loop for testing
for item in range(0, 4):

    # get shape and check that it's valid
    what_shape = choice_checker("Shape? ", valid_shapes, "Please enter a valid shape\n")
    print()
