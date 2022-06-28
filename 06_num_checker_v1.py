import math

summary_list = []

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
def do_math():

    what_shape = choice_checker("Shape? ", valid_shapes, "Please enter a valid shape\n")
    print()

    # get dimensions and do math

    if what_shape == "square":
        base = int_check("Enter a side: ", "Please enter a number more than 0", float)

        # --- area ---
        area = base * base
        # --- perimeter ---
        perimeter = 4 * base

        summary = "Question {}: Shape: Square | A side: {}\n" \
                  "Area = {} | Perimeter = {}\n".format(num_questions + 1, base, area, perimeter)

    elif what_shape == "rectangle":
        base = int_check("Base: ", "Please enter a number more than 0", float)
        height = int_check("Height: ", "Please enter a number more than 0", float)

        # --- area ---
        area = base * height
        # --- perimeter ---
        perimeter = 2 * base + 2 * height

        summary = "Question {}: Shape: Rectangle | Base: {}, Height: {}\n" \
                  "Area = {} | Perimeter = {}\n".format(num_questions + 1, base, height, area, perimeter)

    elif what_shape == "circle":
        radius = int_check("Radius: ", "Please enter a number more than 0", float)

        # --- area ---
        area = math.pi * radius * radius
        # --- perimeter ---
        perimeter = 2 * math.pi * radius

        summary = "Question {}: Shape: Circle | Radius: {}\n" \
                  "Area = {} | Perimeter = {}\n".format(num_questions + 1, radius, area, perimeter)

    else:
        base = int_check("Base: ", "Please enter a number more than 0", float)
        height = int_check("Height: ", "Please enter a number more than 0", float)
        side_2 = int_check("Side 2: ", "Please enter a number more than 0", float)
        side_3 = int_check("Side 3: ", "Please enter a number more than 0", float)

        # --- area ---
        area = 0.5 * base * height
        # --- perimeter ---
        perimeter = base + side_2 + side_3

        summary = "Question {}: Shape: Triangle | Base: {}, Height: {}, Side 2: {}, Side 3: {}\n" \
                  "Area = {} | Perimeter = {}\n".format(num_questions + 1, base, height, side_2, side_3, area, perimeter)

    # print summary after every question
    quick_summary = "Area = {} | Perimeter = {}\n".format(area, perimeter)
    print(quick_summary)

    summary_list.append(summary)

    return ""


# Main Routine...

# setup list
valid_shapes = ["square", "rectangle", "circle", "triangle"]
yes_no_list = ["yes", "no"]
num_questions = 0

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

    # ask user for shape and do the math
    do_math()

    # add one to question counter
    num_questions += 1

# summary
see_summary = choice_checker("Would you like to see the summary? ", yes_no_list, "Please enter yes or no ")

# if the user wants to see the summary print it
if see_summary == "yes":

    print()
    for summary in summary_list:
        print(summary)
