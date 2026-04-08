print("Welcome to my computer quiz!")

playing = input("Do you want to play?")

if playing.lower() != "yes":
    quit()
print("Okay! Let's play :)")
score = 0 
answer = input ("What does CPU stand for? ") 
print("You answered: " + answer) # Central PROCESSING UniT
print("You answered: " + answer.upper())  # central processing unit
if answer.upper() =="CENTRAL PROCESSING UNIT":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

answer = input ("What does GPU stand for? ")
print("You answered: " + answer) # Graphics Processing Unit
print("You answered: " + answer.lower())  # graphics processing unit
if answer.lower() =="graphics processing unit":
    print("Correct!")
    score+=1
else:    print("Incorrect!")     

answer = input ("What does RAM stand for? ")
print("you answered: " + answer) # Random Access Memory
print("You answered: " + answer.title())  # Random Access Memory
if answer.title() =="Random Access Memory":    
    print("Correct!")
    score+=1
else:    
    print("Incorrect!")    

print("You got " + str(score) + " questions correct!")
print("You got " + str((score/4)*100) + "%.")
