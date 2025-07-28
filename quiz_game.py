print("Welcome to my computer quiz")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")

score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
        
answer = input("What does PSU stand for? ")
if answer.lower() == "power supply unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
    
answer = input("What does USA stand for? ")
if answer.lower() == "united state of america":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
    
answer = input("What does GTG stand for? ")
if answer.lower() == "good to go":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("what is name of the developer of this game? ")
if answer.lower() == "toba":
    print("correct!")
    score +=1
else:
    print("Incorrect!")


print("you got " + str(score) + " questions correctly!")
print("you got " + str((score/7)*100) + "%")
