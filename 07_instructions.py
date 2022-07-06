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


# holds instruction information
def instructions():

    print("- First you will be asked how many questions you need to answer (press [enter] for infinite questions and"
          "type 'xxx' to break the loop when asked for a shape).\n"
          "- You will then be asked to enter a shape (square, rectangle, triangle or circle).\n"
          "- Based on the shape you will be asked for the appropriate dimensions (these dimensions can be decimals).\n"
          "- The program will then print out the area and perimeter before beginning the loop again.\n"
          "- Once you have answered your desired amount of questions the program will ask if you want to see a summary.\n"
          "- This shows all your questions that you answered in one easy to read table.")


# main routine
yes_no_list = ["yes", "no"]

for item in range(1, 3):
    see_instructions = choice_checker("Instructions? ", yes_no_list, "Please enter yes or no")

    if see_instructions == "yes":
        print()
        instructions()
    else:
        print("\nProgram Begins")
