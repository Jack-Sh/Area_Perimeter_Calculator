# functions


# Checks for an integer more than 0
def int_check(question):

    error = "Please enter a whole number that is more than 0\n"

    valid = False
    while not valid:

        # ask user for number and check it is valid
        try:
            response = int(input(question))

            # if the response is zero or lower print an error
            if response <= 0:
                print(error)

            # if the response is greater than zero, the code continues
            else:
                return response

        # if an integer is not entered, display an error
        except ValueError:
            print(error)


# main routine
questions_needed = input("How many questions do you need to answer? ")

if questions_needed == "":
    questions_needed = 1000

else:
    int_check(questions_needed)

print("\n---- Program Launches ----")
print()

num_questions = int(questions_needed)

while num_questions != 0:

    side_1 = input("Side 1? ")
    print()
    num_questions -= 1