print("Welcome to the Hogwarts Sorting Hat")

trait = input("What best describes you? ").lower()
brave = input("Are you brave? ").lower()
intelligent = input("Are you intelligent?").lower()
bravery = int(input("How brave are you? (1-10)"))
loyalty = int(input("How loyal are you? (1-10)"))

tired = False

if trait =="brave":
    print("You belong in Gryffindor")
    
elif trait == "intelligent":
    print("You belong in Ravenclaw!")
    
elif trait == "loyal":
    print("You belong in Hufflepuff")
    
elif trait == "ambitious":
    print("You belong in Slytherin")
 
else:
    print("The Sorting Hat is confused")
    
if brave == "yes" and intelligent == "yes":
    print("You could belong in Gryffindor or Ravenclaw!")
    
if (trait == "brave" or trait == "daring") and not tired:
    print("You belong in Gryffindor")
    
if bravery >= 7 and loyalty >=5:
    print("You could belong in Gryffindor or Hufflepuff")                        