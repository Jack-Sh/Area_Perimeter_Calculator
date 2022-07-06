import math
import pandas

# Functions


def int_check(question, error, num_type):
    while True:

        response = input(question)

        if response != "":

            try:
                response = num_type(response)

                if response <= 0:
                    print(error)
                    continue

                else:
                    return response

            except ValueError:
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
def do_math(shape):

    # get dimensions and do math

    if shape == "square":
        side_1 = int_check("Enter a side: ", "Please enter a number more than 0", float)

        # --- area ---
        area = side_1 * side_1
        # --- perimeter ---
        perimeter = 4 * side_1

        # set other sides to / for the lists
        side_2 = "/"
        side_3 = "/"

    elif shape == "rectangle":
        side_1 = int_check("Base: ", "Please enter a number more than 0", float)
        side_2 = int_check("Height: ", "Please enter a number more than 0", float)

        # --- area ---
        area = side_1 * side_2
        # --- perimeter ---
        perimeter = 2 * side_1 + 2 * side_2

        # set other sides to / for the lists
        side_3 = "/"

    elif shape == "circle":
        side_1 = int_check("Radius: ", "Please enter a number more than 0", float)

        # --- area ---
        area = math.pi * side_1 * side_1
        # --- perimeter ---
        perimeter = 2 * math.pi * side_1

        # set other sides to / for the lists
        side_2 = "/"
        side_3 = "/"

    else:
        side_1 = int_check("Side 1: ", "Please enter a number more than 0", float)
        side_2 = int_check("Side 2: ", "Please enter a number more than 0", float)
        side_3 = int_check("Side 3: ", "Please enter a number more than 0", float)

        # --- perimeter ---
        perimeter = side_1 + side_2 + side_3

        # --- area ---
        semi_perim = perimeter/2
        area_unsquared = (semi_perim - side_1) * (semi_perim - side_2) * (semi_perim - side_3) * semi_perim
        area = math.sqrt(area_unsquared)

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

    print("- First you will be asked how many questions you need to answer (press [enter] for infinite questions and"
          "type 'xxx' to break the loop when asked for a shape).\n"
          "- You will then be asked to enter a shape (square, rectangle, triangle or circle).\n"
          "- Based on the shape you will be asked for the appropriate dimensions (these dimensions can be decimals).\n"
          "- The program will then print out the area and perimeter before beginning the loop again.\n"
          "- Once you have answered your desired amount of questions the program will ask if you want to see a summary.\n"
          "- This shows all your questions that you answered in one easy to read table.")


# setup lists
valid_shapes = ["square", "rectangle", "circle", "triangle"]
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
see_instructions = choice_checker("Do you want to see the instructions? ", yes_no_list, "Please enter yes or no")

# if user enters "yes" print instructions
if see_instructions == "yes":
    print()
    instructions()

# Ask how many question the user needs to answer
questions_needed = int_check("How many questions do you need to answer? ", "Please enter a num more than 0 or [enter]",
                             int)

if questions_needed == "":
    questions_needed = 1000

# Program Begins
print("\n---- Program Launches ----")
print()


# Start loop (while the number of questions doesn't equal the max questions)
while num_questions != questions_needed:

    # print the question number
    print("--- Question: {} ---".format(num_questions + 1))

    what_shape = choice_checker("Shape? ", valid_shapes, "Please enter a valid shape\n")
    print()

    all_shapes.append(what_shape)

    if what_shape == "xxx":
        break

    # ask user for shape and do the math
    do_math(what_shape)

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
