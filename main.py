import os
import time
import sys

from time import sleep

type = ""
attacks = []
defenses = []

clear = lambda: os.system('clear')

def game(): 
  def select():
    clear()
    print("Druid: A healer type that uses some ancient magic.")
    print("Hero: A knight with strong armor and a lethal sword.")
    print("Wizard: A mysterious being who attacks with various magical spells.")

    global attacks
    global defenses
    global type

    type = input("Chose your charecter ").lower()
    if type == "wizard":
      attacks = ["Fireball", "Poison splash"]
      defenses = ["Healing spell", "Fire wall"]
    elif type == "hero":
      attacks = ["Throw sheield", "Sword slash"]
      defenses = ["Shield block", "Intense armor"]
    elif type == "druid":
      attacks = ["Sun ray", "Dark beam"]
      defenses = ["Band-Aid power", "Light recovery"]
    else:
      select()
    clear()
    print("Attacks", *attacks, sep = ", ") # * to print all items in array
    print("Defenses", *defenses, sep = ", ") # sep means seperate with
    if input("Type confirm to confirm ").lower() != "confirm":
      clear()
      select()

  select()

  print("Welcome young ", type, " You have been summoned to defeat the evil king")
  print ("You must fight the evil king.")
  print ("Your first mission is to flee your home town")
  print ("To get pass your home town you need defeat the king's henchmen.")
  print("There is henchmen stationed in your town that you need to subdue")
  print("The first thing you need is to identify is who the henchmen is")
  print("Your journy starts now:")

  input("Press enter to continue... ")
  clear()

  print ("You are going about your daily life preparing for your mission when you here a scream")
  print("You go out to investigate and you see someone running away. This person was known to not like the King.")
  print("Could this be one of the henchmen?")
  print("You go to the court case held")
  print("-The victim had gone to a rally for overthrowing the king the day before")
  print("-The victim was not found")
  print("The suposed killer was also not found")
  print("The suposed killer was also at the rally but no one knows why")
  print("There were small prints were the scream was heard")


  def choice1():
    point1 = input("Input yes or no if the suposed killer was actually the killer: ").lower()
    if point1 == "yes":
      print ("WRONG!!!, he was not the killer both him and the victim were fleeing the village and the scream was from them being scared by a cat")
      print ("You try to flee the village but the real henchmen takes you out")
    elif point1 == "no":
      print ("Correct, he was not the killer both him and the victim were fleeing the village and the scream was from them being scared by a cat")
      print ("you now continue your search for the real henchmen")
    else:
      choice1()
      game()
  choice1()

game()
