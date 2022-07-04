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

    elif shape == "rectangle":
        side_1 = int_check("Base: ", "Please enter a number more than 0", float)
        side_2 = int_check("Height: ", "Please enter a number more than 0", float)

        # --- area ---
        area = side_1 * side_2
        # --- perimeter ---
        perimeter = 2 * side_1 + 2 * side_2

    elif shape == "circle":
        side_1 = int_check("Radius: ", "Please enter a number more than 0", float)

        # --- area ---
        area = math.pi * side_1 * side_1
        # --- perimeter ---
        perimeter = 2 * math.pi * side_1

    else:
        side_1 = int_check("Side 1: ", "Please enter a number more than 0", float)
        side_2 = int_check("Side 2: ", "Please enter a number more than 0", float)
        side_3 = int_check("Side 3: ", "Please enter a number more than 0", float)

        # --- area ---
        semi_perim = (side_1 + side_2 + side_3)/2
        area_unsquared = (semi_perim - side_1) * (semi_perim - side_2) * (semi_perim - side_3) * semi_perim
        area = math.sqrt(area_unsquared)

        # --- perimeter ---
        perimeter = side_1 + side_2 + side_3

    all_side_1.append(side_1)
    all_side_2.append(side_2)
    all_side_3.append(side_3)
    all_area.append(area)
    all_perim.append(perimeter)

    # print summary after every question
    quick_summary = "Area = {} | Perimeter = {}\n".format(area, perimeter)
    print(quick_summary)

    return ""


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
