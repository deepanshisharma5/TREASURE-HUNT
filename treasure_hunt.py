#project 8
#TREASURE HUNT GAME

print('''  
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
   ''') 
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
step_1=input(" OH!! You have two ways to go✌...So,Where you want to go ? \n →Left or Right")
if step_1=="Right" or  step_1!="Left":
    print("Fallen into a hole🕳. \n GAME OVER")
else :
    step_2=input("GOOD CHOICE👍.. \n We detect a water body near you🌊. \n OH! that's a river🏞 we see. \n  So would you like to 'Swim' or 'Wait' for a boat ⛵?")
    if step_2=="Swim":
        print("Oh no 😔.. \n  You are Attacked by Trouts. 😰 \n  GAME OVER")
    else:
        step_3=input("GOOD CHOICE 👍..\n  Oh ...we see some colourful doors 🚪... That's some bright colours we see...\n We have  three doors 'Red' , 'Blue' and 'Yellow'. \n Which door you want to choose?")
        if step_3=="Red":
            print("Oh no 😔..\n You are burned by fire 🔥\n GAME OVER")
        elif step_3=="Blue":
            print("Oh no 😔..\n You are eaten by beasts ☠ \n GAME OVER")
        elif step_3=="Yellow":
            print("YOU WIN🎉🎉 \n YOU'VE GOT THE TREASURE HUNT 🎁🎉 \n GAME OVER")
