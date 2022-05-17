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


# Main routine

# ask how many question the user needs to answer
questions_needed = input("How many questions do you need to answer? ")

# if user types [enter] set questions to 1000 (for now)
if questions_needed == "":
    questions_needed = 1000

# if users enters a number check that it's valid
else:
    int_check(None, questions_needed)

# program begins
print("\n---- Program Launches ----")
print()

# define number of questions and ensure that questions needed is a integer
num_questions = int(questions_needed)

# start loop (while number of questions does not = 0)
while num_questions != 0:

    # ask for side 1
    side_1 = input("Side 1? ")
    print()

    # if user enters xxx break the loop
    if side_1 == "xxx":
        break

    # subtract 1 from the questions counter
    num_questions -= 1
