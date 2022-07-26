import math
import pandas


# Functions


# rounds to 2dp
def rounding(x):
    return "{:.2f}".format(x)


# checks if a number is valid
def num_check(question, num_type, allow_enter):
    error = "Please enter a number more than 0"

    # start loop
    while True:

        # ask question
        response = input(question)

        # if the response does not equal [enter]
        if response != "":

            # ask question with given num_type (float, int)
            try:
                response = num_type(response)

                # if the response is less than or equal to zero print error
                if response <= 0:
                    print(error)
                    continue

                # otherwise, return the response
                else:
                    return response

            # print error for unexpected values and restart the loop
            except ValueError:
                print(error)
                continue

        # if user types [enter] and allow_enter is set to no, print an error and start the loop again
        else:
            if allow_enter == "no":
                print(error)
                continue

        return response


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


# Ask user for shape, do math then create the output for summary
def do_math(shape, rounded_answers):

    # get dimensions and do math

    if shape == "square":
        side_1 = num_check("Enter a side: ", float, "no")

        # --- area ---
        area = side_1 * side_1
        # --- perimeter ---
        perimeter = 4 * side_1

        # set other sides to / for the lists
        side_2 = "/"
        side_3 = "/"

    elif shape == "rectangle":
        side_1 = num_check("Base: ", float, "no")
        side_2 = num_check("Height: ", float, "no")

        # --- area ---
        area = side_1 * side_2
        # --- perimeter ---
        perimeter = 2 * side_1 + 2 * side_2

        # set other sides to / for the lists
        side_3 = "/"

    elif shape == "circle":
        side_1 = num_check("Radius: ", float, "no")

        # --- area ---
        area = math.pi * side_1 * side_1
        # --- perimeter ---
        perimeter = 2 * math.pi * side_1

        # set other sides to / for the lists
        side_2 = "/"
        side_3 = "/"

    else:
        # ask user what dimensions they have
        check_dimensions = choice_checker("Do you just have base and height? ", yes_no_list, "Please enter yes or no\n")
        print()

        # set sides values for loop
        side_1 = 0
        side_2 = 0
        side_3 = 1

        # if user has 3 side values...
        if check_dimensions == "no":

            # set up loop (while the sum of 1 + 2 is lesser than or equal to 3
            while side_1 + side_2 <= side_3:

                # get dimension values
                side_1 = num_check("Side 1: ", float, "no")
                side_2 = num_check("Side 2: ", float, "no")
                side_3 = num_check("Side 3: ", float, "no")

                # print error if it is an impossible triangle
                if side_1 + side_2 <= side_3:
                    print("This is an impossible triangle. The sum of side 1 + side 2 must be greater than side 3\n")
                    continue

            # --- perimeter ---
            perimeter = side_1 + side_2 + side_3

            # --- area ---
            semi_perim = perimeter/2
            area_unsquared = (semi_perim - side_1) * (semi_perim - side_2) * (semi_perim - side_3) * semi_perim
            area = math.sqrt(area_unsquared)

        # if user has base and height get values
        else:
            side_1 = num_check("Base: ", float, "no")
            side_2 = num_check("Height: ", float, "no")
            side_3 = "/"

            # --- area ---
            area = 0.5 * side_1 * side_2

            # set perimeter to blank
            perimeter = "/"

    # round answers if user wants rounding
    if rounded_answers == "yes":
        area = rounding(area)

        if perimeter != "/":
            perimeter = rounding(perimeter)

    # append all data into respective lists
    all_side_1.append(side_1)
    all_side_2.append(side_2)
    all_side_3.append(side_3)
    all_area.append(area)
    all_perim.append(perimeter)

    # print summary after every question
    quick_summary = "Area = {} | Perimeter = {}\n".format(area, perimeter)
    print(quick_summary)

    return ""


# holds instruction information
def instructions():

    print("- Then, you will be asked if you want rounded answers (these will be rounded to 2 dp)\n"
          "- First you will be asked how many questions you need to answer (press [enter] for infinite questions and"
          "type 'xxx' to break the loop when asked for a shape).\n"
          "- You will then be asked to enter a shape (square, rectangle, triangle or circle).\n"
          "- Based on the shape you will be asked for the appropriate dimensions (these dimensions can be decimals).\n"
          "- The program will then print out the area and perimeter before beginning the loop again.\n"
          "- Once you have answered your desired amount of questions the program will ask if you want to see a summary.\n"
          "- This shows all your questions that you answered in one easy to read table.\n")
    print()


# setup lists
valid_shapes = ["square", "rectangle", "circle", "triangle", "xxx"]
yes_no_list = ["yes", "no"]

all_shapes = []
all_side_1 = []
all_side_2 = []
all_side_3 = []
all_area = []
all_perim = []

num_questions = 0

# setup dictionaries
summary_data_dict = {
    "Shape": all_shapes,
    "Length 1": all_side_1,
    "Length 2": all_side_2,
    "Length 3": all_side_3,
    "Area": all_area,
    "Perimeter": all_perim
}

# ask user if they want instructions
see_instructions = choice_checker("Do you want to see the instructions? ", yes_no_list, "Please enter yes or no\n")
print()

# if user enters "yes" print instructions
if see_instructions == "yes":
    instructions()

# ask user if they want rounded answers
do_rounding = choice_checker("Do you want rounded answers? (2dp) ", yes_no_list, "Please enter yes or no\n")
print()

# Ask how many question the user needs to answer
questions_needed = num_check("How many questions do you need to answer? ", int, "yes")

if questions_needed == "":
    questions_needed = 1000

# Start loop (while the number of questions doesn't equal the max questions)
while num_questions != questions_needed:

    # print the question number
    print()
    print("--- Question: {} ---".format(num_questions + 1))

    # ask user for shape
    what_shape = choice_checker("Shape? ", valid_shapes, "Please enter a valid shape (square, rectangle, circle, triangle)\n")
    print()

    # if user enters xxx break loop
    if what_shape == "xxx":
        break

    # add shape to list
    all_shapes.append(what_shape)

    # call the function and set round answers to yes or no
    if do_rounding == "yes":
        do_math(what_shape, "yes")

    else:
        do_math(what_shape, "no")

    # add one to question counter
    num_questions += 1

# create data frame and order columns
summary_frame = pandas.DataFrame(summary_data_dict, columns=['Shape', 'Length 1', 'Length 2',
                                                             'Length 3', 'Area', 'Perimeter'])

# ask user if they want to see the summary
see_summary = choice_checker("Do you want to see the summary? ", yes_no_list, "Please enter yes or no")

# if yes print the summary
if see_summary == "yes":
    print()
    print(summary_frame)
