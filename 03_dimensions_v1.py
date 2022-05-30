# functions


# Checks for an integer more than 0
def int_check(question=None, num=None):

    # custom error message
    error = "Please enter a whole number that is more than 0\n"

    # define situation
    situation = ""

    # if user has specified a question and not a number
    # then the situation is question only
    if question is not None and num is None:
        situation = "question only"

    # if user has specified number and not question
    # then the situation is number only
    elif question is None and num is not None:
        situation = "num only"

    # start the loop
    valid = False
    while not valid:

        try:
            # if the situation is question only ask for number
            if situation == "question only":

                response = int(input(question))

                # if the response is zero or lower print an error
                if response <= 0:
                    print(error)

                # if the response is greater than zero, the code continues
                else:
                    return response

            # if the situation is number only
            else:
                # change the string to an integer
                num = int(num)
                # if the response is zero or lower print an error
                if num <= 0:
                    print(error)

                # if the response is greater than zero, the code continues
                else:
                    return num

        # if an integer is not entered, display an error
        except ValueError:
            print(error)


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
    what_shape = choice_checker("Shape? ", valid_shapes, "Please enter a valid shape\n")

    if what_shape == "rectangle" or what_shape == "square":

        base = int_check("Enter Base Length: ", None)
        height = int_check("Enter Height Length: ", None)
        print("Base = {} | Height = {} ".format(base, height))
        print()

    elif what_shape == "triangle":

        base = int_check("Enter Base Length: ", None)
        height = int_check("Enter Height Length: ", None)
        side_2 = int_check("Enter Side 2 Length: ", None)
        side_3 = int_check("Enter Side 3 Length: ", None)
        print("Base = {} | Height = {} | Side 2 = {} | Side 3 = {}".format(base, height, side_2, side_3))

    else:
        radius = int_check("Enter Radius: ", None)
        print("Radius {}".format(radius))