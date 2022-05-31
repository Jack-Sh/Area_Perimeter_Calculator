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


# Does math for rectangle
def rectangle_function():

    # asks for base and height
    base = int_check("Base: ")
    height = int_check("Height: ")

    # do the math for area and perimeter
    area = base * height
    perimeter = base*2 + height*2

    # print the area and perimeter
    print("Area - {} | Perimeter - {}".format(area, perimeter))
    print()

    # return the area and perimeter
    return area, perimeter


# does math for triangle
def triangle_function():

    # ask for dimensions
    base = int_check("Base: ")
    height = int_check("Height: ")
    side_2 = int_check("Side 2: ")
    side_3 = int_check("Side 3: ")

    # do math
    area = 0.5*base*height
    perimeter = base+side_2+side_3

    # print area and perimeter
    print("Area - {} | Perimeter - {}".format(area, perimeter))
    print()

    # return the area and perimeter
    return area, perimeter


# does math for square
def square_function():

    # ask for dimensions
    side_1 = int_check("Enter a side: ")

    # do math
    area = side_1*side_1
    perimeter = side_1*4

    # print area and perimeter
    print("Area - {} | Perimeter - {}".format(area, perimeter))
    print()

    # return area and perimeter
    return area, perimeter


def circle_function():

    # ask for dimensions
    radius = int_check("Radius: ")

    # do math
    area =


# main routine

# setup list
valid_shapes = ["square", "rectangle", "circle", "triangle"]

# begin loop
for item in range(0,4):

    # get shape and check that it's valid
    what_shape = choice_checker("Shape? ", valid_shapes, "Please enter a valid shape\n")
    print()

    # if the chosen shape is a rectangle run the correct function
    if what_shape == "rectangle":
        rectangle_function()

    elif what_shape == "triangle":
        triangle_function()

    elif what_shape == "square":
        square_function()