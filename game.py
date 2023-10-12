#Gian Cyrus F. Salvador
#CITCS-1B Game for Finals.
#game thing for finals. Dunno how to fix some parts of it but yeah.
#its still a super beta thing but i am trying.

#Copied this in StackOverflow: https://stackoverflow.com/questions/4099422/printing-slowly-simulate-typing
#Have to credit the creator yo.
import sys,time,random

typing_speed = 50 #wpm
def slow_type(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)
    print ('')

slow_type("Hello.")
NAME_OF_PLAYER = input("What is your name? ")
slow_type(f"I see, {NAME_OF_PLAYER}. A wonderful name.")
print("")
TITLE_OF_PLAYER = input("What should we call you? ")
print("")
slow_type(f"Congrats on being chosen {TITLE_OF_PLAYER}, You are to help the people on board the Catalyst-C01")
print("")
slow_type("You will receive the details shortly.")
print("")
slow_type(f"Throughout this transmission you should know what to do {TITLE_OF_PLAYER}, We will not help you.")
slow_type(f"IF they say things you do not understand, END THE TRANSMISSION IMMEDIATELY {TITLE_OF_PLAYER}.")
print("")
slow_type("Do you UNDERSTAND?")
USER_ANSWER = input("Yes/No? ")

YES_cHOICES = ['Yes', 'yes', 'Y', 'y']
NO_CHOICES = ['No', 'no', 'N', 'n']

if USER_ANSWER.lower() in YES_cHOICES:
    print("Good. You Understand. We have a policy here to avoid contact with any anomalies.")
elif USER_ANSWER.lower() in NO_CHOICES:
    print("Even basic instructions you don't understand? You are a liability.")
else:
    print(f"Answer me correctly {TITLE_OF_PLAYER}.")

print("")

slow_type("You will be connected shortly with Catalyst-C01")
slow_type("Best of luck to you.")

print("")