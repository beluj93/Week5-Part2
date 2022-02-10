# Import random library
from random import randrange
# Set the variables that will be introduced and used in the game
steps = 10
ammo = 3
health = 3
duck = 0
rabbit = 0
squirrel = 0
trophy_buck = 0
shot = 1

# Prompt the user: name and birthdate before playing this game
hunter = input("What is your name? ")
# Age restriction, user must be at least 18 years of age in order to continue.
age = int(input("How old are you? "))
if age <= 17:
    print("Sorry! You must be at least 18 years or older to play this game.")
    print()
    exit()

print("Welcome to the hunter explorer {}! You have 3 lives and 3 ammos to start out with to shoot your trophy buck. Good Luck!".format(hunter))
print()

# Create a class for Adventure Game
class Game():
# Define the main function that will kick start the game
    def main():
        global ammo
        global health
        global duck
        print("{} is hunting and then heard noises just 10 steps in front of you.".format(hunter))
        user = input("Only 10 steps left. Step forward (y/n)? ")
        print()
# Define 3 random choices if user input 'y'         
        if user == 'y':
            choice = randrange(1, 4)
            if choice == 1:
                print("You have been bitten by a snake! You lose 1 life")
                health -= 1
                print("You have {} lives left.".format(health))
                print()
            elif choice == 2:
                print("You collected +1 ammo!")
                ammo += 1
                print("You have {} ammo left".format(ammo))
                print()
            elif choice == 3:
                print("You shot a duck! Harvested 1 duck")
                duck += 1
                print("You have {} duck left".format(duck))
                ammo -= 1
                print("You have {} ammo left.".format(ammo))
                print()
                
        if user == 'n':
            choice2 = randrange(1,4)
            if choice2 == 1:
                print("You waited and obtained +4 ammo.")
                ammo += 2
                print("You have {} ammo left.".format(ammo))
                print()
            elif choice2 == 2:
                print("You found and ate poison mushroom. You lose 1 life")
                health -= 1
                print("You have {} lives left.".format(health))
                print()
            elif choice2 == 3:
                print("You shot a rabbit and missed. -1 ammo")
                ammo -= 1
                print("You have {} ammo left.".format(ammo))
                print()
    main()
# Create another function to continue the game
    def body():
        global ammo
        global health
        global steps
        global rabbit
        global squirrel
        print("{} is hunting and then heard noises just 8 steps in front of you.".format(hunter))
        steps -= 2
        user = input("Only {} steps left. Step forward (y/n)? ".format(steps))
        print()
# Define 3 random choices if user input 'y'         
        if user == 'y':
            choice = randrange(1, 4)
            if choice == 1:
                print("You have been bitten by a cougar! You lose 2 life")
                health -= 2
                print("You have {} lives left.".format(health))
                print()
                if health <= 0:
                    print("{} has run out of lives. Game Over!".format(hunter))
                    exit()
            elif choice == 2:
                print("You collected +1 ammo!")
                ammo += 1
                print("You have a total of {} ammo".format(ammo))
                print()
            elif choice == 3:
                print("You shot a rabbit! Harvested 1 rabbit")
                rabbit += 1
                print("You have {} rabbit left".format(rabbit))
                ammo -= 1
                print("You have {} ammo left".format(ammo))
                print()
                if ammo <= 0:
                    print("{} has run out of ammo. Game Over!".format(hunter))
                    exit()      
        if user == 'n':
            choice2 = randrange(1,4)
            if choice2 == 1:
                print("You shot a squirrel! Harvested 1 squirrel ")
                squirrel += 1
                print("You have {} squirrel left".format(squirrel))
                ammo -= 1
                print("You have {} ammo left".format(ammo))
                print()
                if ammo <= 0:
                    print("{} has run out of ammo. Game Over!".format(hunter))
                    exit()
            elif choice2 == 2:
                print("You fell into a hole and lost 1 life")
                health -= 1
                print("You have {} lives left.".format(health))
                print()
                if health <= 0:
                    print("{} has run out of lives. Game Over!".format(hunter))
                    print("{} has run out of health. Game Over!".format(hunter))
                    exit()               
            elif choice2 == 3:
                print("You shot a squirrel and missed. -1 ammo")
                ammo -= 1
                print("You have {} ammo left.".format(ammo))
                print()
                if ammo <= 0:
                    print("{} has run out of ammo. Game Over!".format(hunter))
                    exit()
    body()
# Create another function to continue the game
    def body1():
        global ammo
        global health
        global steps
        global duck
        global squirrel
        print("{} is hunting and then heard noises just 6 steps in front of you.".format(hunter))
        steps -= 2
        user = input("Only {} steps left. Step forward (y/n)? ".format(steps))
        print()
# Define 3 random choices if user input 'y'         
        if user == 'y':
            choice = randrange(1, 4)
            if choice == 1:
                print("You found +2 ammo")
                ammo += 2
                print("You have {} ammo left.".format(ammo))
            elif choice == 2:
                print("You shot 2 squirrel and missed 1. Harvested 1 squirrel")
                squirrel += 1
                print("You have {} squirrel left".format(squirrel))
                ammo -= 2
                print("You have a total of {} ammo".format(ammo))
                print()
                if ammo <= 0:
                    print("{} has run out of ammo. Game Over!".format(hunter))
                    exit()
            elif choice == 3:
                print("You shot a duck! Harvested 1 duck")
                duck += 1
                print("You have {} duck left".format(duck))
                ammo -= 1
                print("You have a total of {} ammo".format(ammo))
                print()
                if ammo <= 0:
                    print("{} has run out of ammo. Game Over!".format(hunter))
                    exit()
        if user == 'n':
            choice2 = randrange(1,4)
            if choice2 == 1:
                print("You ate and slept. Recover +2 health")
                health += 2
                print("You have {} lives left".format(health))
                print()
            elif choice2 == 2:
                print("You found a forest fire. Damage to life -2 ")
                health -= 2
                print("You have {} lives left.".format(health))
                print()
            elif choice2 == 3:
                print("You shot a rabbit. Harvested a rabbit")
                rabbit += 1
                print("You have {} rabbit left.".format(rabbit))
                ammo -= 1
                print("You have {} ammo left.".format(ammo))
                print()
                if ammo <= 0:
                    print("{} has run out of ammo. Game Over!".format(hunter))
                    exit()
    body1()
# Create another function to continue the game
    def body2():
        global ammo
        global health
        global steps
        global duck
        global squirrel
        print("{} is hunting and then heard noises just 4 steps in front of you.".format(hunter))
        steps -= 2
        user = input("Only {} steps left. Step forward (y/n)? ".format(steps))
        print()
# Define 3 random choices if user input 'y'         
        if user == 'y':
            choice = randrange(1, 4)
            if choice == 1:
                print("You shot 2 squirrels, with 2 ammo")
                squirrel += 2
                print("You have {} squirrel left.".format(squirrel))
                ammo -= 2
                print("You have a total of {} ammo".format(ammo))
                print()
                if ammo <= 0:
                    print("{} has run out of ammo. Game Over!".format(hunter))
                    exit()
            elif choice == 2:
                print("You collected +2 ammo!")
                ammo += 2
                print("You have a total of {} ammo".format(ammo))
                print()
            elif choice == 3:
                print("You shot a duck! Harvested 1 duck")
                duck += 1
                print("You have {} duck left".format(duck))
                ammo -= 1
                print("You have {} ammo left".format(ammo))
                print()
                if ammo <= 0:
                    print("{} has run out of ammo. Game Over!".format(hunter))
                    exit()
        if user == 'n':
            choice2 = randrange(1,4)
            if choice2 == 1:
                print("You tripped over a log and lost -2 ammo")
                ammo -= 2
                print("You have {} ammo left".format(ammo))
                print()
                if ammo <= 0:
                    print("{} has run out of ammo. Game Over!".format(hunter))
                    exit()
            elif choice2 == 2:
                print("You found some water and gained +2 life")
                health += 2
                print("You have {} lives left.".format(health))
                print()
            elif choice2 == 3:
                print("You shot a rabbit and missed. -1 ammo")
                ammo -= 1
                print("You have {} ammo left.".format(ammo))
                print()
                if ammo <= 0:
                    print("{} has run out of ammo. Game Over!".format(hunter))
                    exit()
    body2()
# Create another function to continue the game  
    def body3():
        global ammo
        global health
        global steps
        global duck
        global rabbit
        global squirrel
        print("{} is hunting and then heard noises just 2 steps in front of you.".format(hunter))
        steps -= 2
        user = input("Only {} steps left. Step forward (y/n)? ".format(steps))
        print()
# Define 3 random choices if user input 'y'       
        if user == 'y':
            choice = randrange(1, 4)
            if choice == 1:
                print("You were attacked by a bear and lost all your health. Game Over!")
                print("End Health: {} ".format(health))
                print("End Ammo: {} ".format(ammo))
                print("End Harvested:{} duck, {} rabbit, {} squirrel".format(duck, rabbit, squirrel))
                print("{} has run out of lives. Game Over!".format(hunter))
                exit()
            elif choice == 2:
                print("You collected +1 ammo!")
                ammo += 1
                print("You have a total of {} ammo".format(ammo))
                print()
            elif choice == 3:
                print("You shot a duck! Harvested 1 duck")
                duck += 1
                print("You have {} duck left".format(duck))
                ammo -= 1
                print("You have {} ammo left".format(ammo))
                print()
                if ammo <= 0:
                    print("{} has run out of ammo. Game Over!".format(hunter))
                    exit()

        if user == 'n':
            choice2 = randrange(1,4)
            if choice2 == 1:
                print("You found +2 ammo")
                ammo += 2
                print("You have {} ammo left.".format(ammo))
                print()
            elif choice2 == 2:
                print("You found and ate some worms. You gain 1 life")
                health += 1
                print("You have {} lives left.".format(health))
                print()
            elif choice2 == 3:
                print("You shot a rabbit and missed. -1 ammo")
                ammo -= 1
                print("You have {} ammo left.".format(ammo))
                print()
                if ammo <= 0:
                    print("{} has run out of ammo. Game Over!".format(hunter))
                    exit()
    body3()
# Accumulate all the results in last function     
    def body4():
        global ammo
        global health
        global steps
        global shot
        print("{} you're hunting and you finally saw your trophy buck. You only have {} ammo left to harvest your trophy buck. Pick a number from 1-10 to aim and shoot. Good Luck!".format(hunter, ammo))
        steps -= 2
        print()

        bullseye = randrange(1,10)
        aim = int(input("Enter your first number: "))
        ammo == aim
        ammo -= 1
        while aim != bullseye:
            ammo -= 1
            if ammo <= 0:
                print("{} has run out of lives. Game Over!".format(hunter))
                print("You have {} ammo left. Game Over!".format(ammo))
                exit()
            elif aim < bullseye:
                print("Your shot was too low. Aim higher.")
                aim = int(input("Shoot again: "))
                shot += 1
            elif aim > bullseye:
                print("Your shot was too high. Aim lower.")
                aim = int(input("Shoot again: "))
                shot += 1
# Print out the outputs and results of the game that was accumulated throughout the game
        print()
        print("Congratulations {}! You shot your Trophy buck!".format(hunter))
        print("It only took you {} shots".format(shot))
        print("You have {} duck, {} rabbit, {} squirrel, {} life, {} ammo left.".format(duck, rabbit, squirrel, health, ammo))
    body4()


