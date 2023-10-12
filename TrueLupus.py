#Gian Cyrus F. Salvador
#CITCS-1B
#Code Notes.

#Name Input
NAME = input("What is your name? ")
print(f"Hello {NAME}, Nice to meet you!")
LAST_NAME = input("Do you have a last name? ")
print(f"Oh? {LAST_NAME}? That is Wonderful!")

print("")

#AGE Input + Calulator
CURRENT_AGE = int(input("How old are you? "))
ADDITIONAL_NUMBER = int(input("How many years you wanna see bro? "))
AGE_IN_FUTURE = (CURRENT_AGE + ADDITIONAL_NUMBER)
print(f"You will be {AGE_IN_FUTURE} in {ADDITIONAL_NUMBER} year(s)!")
if AGE_IN_FUTURE >= 18:
    print("Looking forward to working with you.")
else:
    print("Too Young bro. END OF TRANSMISSION.")

print("")

#Calculator-ish
DENOMINATOR = float(input("Prototype Division Denominator: "))
NOMINATOR = float(input("Prototype Division Nominator: "))
FINAL_ANSWER = (DENOMINATOR / NOMINATOR)
print(f"The output is {FINAL_ANSWER}. Are you satisfied with the results?")
USER_ANSWER = input("Yes/No? ")

YES_cHOICES = ['Yes', 'yes', 'Y', 'y']
NO_CHOICES = ['No', 'no', 'N', 'n']

if USER_ANSWER.lower() in YES_cHOICES:
    print("thanks dude")
elif USER_ANSWER.lower() in NO_CHOICES:
    print("Alright get out")
else:
    print(f"Answer me correctly {NAME}.")

print("")