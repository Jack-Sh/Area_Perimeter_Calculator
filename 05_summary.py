import math

summary_list = []

# Functions


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
                    continue

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
                    continue

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


# Ask user for shape, do math then create the output for summary
def do_math():

    what_shape = choice_checker("Shape? ", valid_shapes, "Please enter a valid shape\n")
    print()

    # get dimensions and do math

    if what_shape == "square":
        base = int_check("Enter a side: ")

        # --- area ---
        area = base * base
        # --- perimeter ---
        perimeter = 4 * base

        summary = "Question {}: Shape: Square | A side: {}\n" \
                  "Area = {} | Perimeter = {}\n".format(num_questions + 1, base, area, perimeter)

    elif what_shape == "rectangle":
        base = int_check("Base: ")
        height = int_check("Height: ")

        # --- area ---
        area = base * height
        # --- perimeter ---
        perimeter = 2 * base + 2 * height

        summary = "Question {}: Shape: Rectangle | Base: {}, Height: {}\n" \
                  "Area = {} | Perimeter = {}\n".format(num_questions + 1, base, height, area, perimeter)

    elif what_shape == "circle":
        radius = int_check("Radius: ")

        # --- area ---
        area = math.pi * radius * radius
        # --- perimeter ---
        perimeter = 2 * math.pi * radius

        summary = "Question {}: Shape: Circle | Radius: {}\n" \
                  "Area = {} | Perimeter = {}\n".format(num_questions + 1, radius, area, perimeter)

    else:
        base = int_check("Base: ")
        height = int_check("Height: ")
        side_2 = int_check("Side 2: ")
        side_3 = int_check("Side 3: ")

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
questions_needed = input("How many questions do you need to answer? ")

# If user types [enter] set questions to 1000 (for now)
if questions_needed == "":
    questions_needed = 1000

# If users enters a number check that it's valid
else:
    int_check(None, questions_needed)

# Program Begins
print("\n---- Program Launches ----")
print()

# convert the string questions needed into an int max questions
max_questions = int(questions_needed)

# Start loop (while the number of questions doesn't equal the max questions)
while num_questions != max_questions:

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
