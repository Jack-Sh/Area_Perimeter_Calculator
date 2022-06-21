import math


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


# Ask user for shape and does math
def do_math():

    what_shape = choice_checker("Shape? ", valid_shapes, "Please enter a valid shape\n")
    print()

    # get dimensions

    if what_shape == "square":
        base = int_check("Enter a side: ")
        height = base

    elif what_shape == "rectangle":
        base = int_check("Base: ")
        height = int_check("Height: ")

    elif what_shape == "circle":
        radius = int_check("Radius: ")

    else:
        base = int_check("Base: ")
        height = int_check("Height: ")
        side_2 = int_check("Side 2: ")
        side_3 = int_check("Side 3: ")

    # do math

    # area
    if what_shape == "square" or what_shape == "rectangle":
        area = base * height

    elif what_shape == "triangle":
        area = 0.5 * base * height

    else:
        area = math.pi * radius * radius

    # perimeter
    if what_shape == "square" or what_shape == "rectangle":
        perimeter = 2 * base + 2 * height

    elif what_shape == "triangle":
        perimeter = base + side_2 + side_3

    else:
        perimeter = 2 * math.pi * radius

    # print output
    print("Area = {} | Perimeter = {}".format(area, perimeter))
    print()

# main routine

# setup list
valid_shapes = ["square", "rectangle", "circle", "triangle"]

# begin loop
for item in range(0,4):
    do_math()