import os

type = ""
attacks = []
defenses = []

clear = lambda: os.system('clear')

def select():
  print("Druid: A healer type that uses some ancient magic.")
  print("Hero: A knight with strong armor and a lethal sword.")
  print("Wizard: A mysterious being who attacks with various magical spells.")

  type = input("Chose your charecter ").lower()
  global attacks
  global defenses
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

  print("Attacks", *attacks, sep = ", ") # * to print all items in array
  print("Defenses", *defenses, sep = ", ") # sep means seperate with
  if input("Type confirm to confirm ").lower() != "confirm":
   clear()
   select()

select()
