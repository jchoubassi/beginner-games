
print("Welcome to my first game!")
name = input("what is your name? ")
age = int(input("how old are you? "))
print( "hello", name, "you are", age, "years old.")
health = 10

is_older = age >= 18
print(is_older)
elif age >= 14:
    print("You can play with supervision!")
else:
    print("You are not old enough to play, boo :(")

if age >= 18:
    print("You are old enough to play!")
    yes_play = input("Do you want to play? ").lower()

    if yes_play == "yes":
         print("Let's play, you are starting with", health, "health")
         Left_or_right = input("Here we go! Let's begin... Left or Right (left/right)?)"
                                 if left_or_right == "left":
                                 ans = input("You follow the path and reach a lake... Do swim across or go around (across/around)?")
                                 if ans == "around":
                                  print("you went around and reached the other side of the lake")
                                 elif ans == "across":
                                  print("you managed to get across, but were bit by a fish and lost 5 health"
                                         health -= 5
    

           else:

         print("you did neither and died of starvation, yikes!")


        else:
            print("you fell down a cliff and died, how embarrassing!")
  
  

   
    else:
        print("Lame, byeeee...")

   