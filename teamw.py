roomArray = []
itemArray = []
import time
for i in range(999):
  roomArray.append(False)
  itemArray.append(False)
  
def highLow():
  color = ["blue", "green", "purple", "Teal", "yellow", "red", "gray", "black"]
  veggies = ["cabage","garlic", "cucumber", "patato", "lettuce", "avacodo", "leek", "carrot", "taro", "ginger"]
  desserts = ["fudge", "cake", "cupcake", "pastery", "danish", "sundae", "cookie", "tart", "chocolate", "brownie"]
  combinedList = color + veggies + desserts
  theWord = combinedList 
  theWord = theWord.lower()
  print("I'm thinking of a secret word. Take a guess and I'll tell you if the secret word is before your word or after your word.")
  while True:
    print("guess a word")
    guess = input()
    guess = guess.lower()
    if guess < theWord:
        print("The secret word is after " + str(guess))
    if guess > theWord:
        print("The secret word is before " + str(guess)) 
    if guess == theWord:
        print("You got it!!!!!")
        return

roomArray[200] = "You are in the corner of a room with walls to the north and west of you. Further east in room is a chair, and to the south west there is a tiny window"
roomArray[400] = "you are near a chair and the walls of the room are to the north and east of you. You can see a tiny window to the south west and a door to the far south"
roomArray[301]= "there is a tiny window letting very little light in and there is door to the far east"
roomArray[300] = "there is a wall to the north of you. There is alos a chair the the west, a vhair to the east and a tiny window to the south"
roomArray[201]= "there is walls to both the west and east of you. There is nothing but a tiny window to the east and a bed to the north in this room."
roomArray[401]= "there is a door directly to the east to leave this room. There is also a chair to the north and a tiny window to the west."
roomArray[403] = "you are in the hallway there is a medical cart in front of you. to the east is the main lobby"
roomArray[501] = "you are now in the main lobby. to the west is your room, you can go east or south"
roomArray[502] = "you're in the middle of the lobby. you can move north, east, and south"
roomArray[503] = "you are in the southern most part of the lobby. you can move west, east, or north"
roomArray[601] = "you are in the corner of the room. you can move west, or south"
roomArray[602] = "you are at the main desk. you can move north, west, and south"
roomArray[603] = "you are in the southeast corner. you can move west or north"
roomArray[405] = "you have found a computer that can be hacked for more hospital information. type 'Hack' to attempt to hack the computer.. you can move west or south"
roomArray[203] = highLow() 
roomArray[303] = "Your in anemptry room with walls north and south of you"
roomArray[204] = "You are in an empty hallway. You may only move north and south."
roomArray[205]= "You are in an empty hallway. There is a blood blank east of you. You may not move west."
roomArray[305] = "You are in a room with a blood bank. There is a special room east of you if you willing to take up the challenge"
roomArray[306]= "Your in an empty room. There is a wall south of you."
roomArray[406]= "You are in a room with many beds around you. You may not move south."
roomArray[506] = "You may only move west. Room north of you may only be entered with the key code."
roomArray[206] = bossBattle()

itemArray[201] = "Pill bottle"
itemArray[300] = "Phone"
itemArray[400] = "coins"
itemArray[602] = "Keycard"
itemArray[403] = "Syringe"
itemArray[603] = "Battery"



def move(userInput, location):
  if str(userInput) == "n" and doesRoomExist(location - 1):
    location = location - 1
  else:
    if str(userInput) == "s" and doesRoomExist(location + 1):
      location = loaction + 1
    else:
      if str(userInput) == "e" and doesRoomExist(location + 100):
        location = location + 100
      else:
        if str(userInput) == "w" and doesRoomExist(location - 100):
          location = location -100
  return location 


def doesRoomExist(roomNumber):
    try:
        if roomArray[roomNumber] == False:
            print ("You can't go there")
            return False
        else: 
            return True
    except:
        print ("You can't go there")
        return False
      
def pickUpItem(location):
  print("would you like to pick it up? type y or n")
  userinput = input()
  if userinput.lower() == "y":
    itemArray[location] = False
    yourItems.append(itemArray[location])
    print("Item Has been picked up")
    return 
  else:
    return
  
def randomHealth(): #bossbattle
    return randint(30,50)

def randomTrueFalse():
    truefalse = randint(1,2)
    if truefalse == 1:
        return True
    else:
        return False

def diceRoll(): #bossbattle
    return randint(1,6)

def hitBoss(weapon, iceWeakness, magicWeakness): #bossbattle
    damage = 0
    weapon = weapon.lower()
    if "sword" in weapon or "spell" in weapon:
        damage = damage + diceRoll()
    if iceWeakness == True and "ice" in weapon:
        damage = damage + diceRoll()
    if iceWeakness == False and "fire" in weapon:
        damage = damage + diceRoll()
    if magicWeakness == True and "spell" in weapon:
        damage = damage + diceRoll()
    if magicWeakness == False and "sword" in weapon:
        damage = damage + diceRoll()
    print("you have done " + str(damage) + " to boss")
    return damage

def hitPlayer(playerHealth): #bossbattle
    EnemyAttacks = ["blades of Blood", "Wind Scarf", "Adamant Barrage", "Telsa attack", "Iron Reaver", "Blacklast Wave", "Revenge Laser"]
    print ("The dragon uses " + choice(EnemyAttacks))
    damage = 0
    damage = damage + diceRoll()
    if playerHealth > 25:
        damage = damage + diceRoll()
    print("the boss did " + str(damage) + " to YOU!")
    return damage

def whoWins(playerHealth, bossHealth): #bossbattle
    if playerHealth <= 0:
        print ("You have been defeated")
    else:
        print("you have defeated the dragon")

def bossBattle(): #bossbattle
  playerHealth = 50
  print("there is a dragon you must defeat in order to pass")
  bossHealth = randomHealth()
  iceWeakness = randomTrueFalse()
  magicWeakness = randomTrueFalse()
  while playerHealth > 0 and bossHealth > 0:
    print("The dragon has " + str(bossHealth) + " health")
    time.sleep(1)
    print("What do you want to use?")
    print("Ice Spell")
    print("Fire Spell")
    print("Ice Sword")
    print("Fire Sword")
    weapon = input()
    time.sleep(1)
    damage = hitBoss(weapon, iceWeakness, magicWeakness)
    bossHealth = bossHealth - damage
    if bossHealth > 0:
      damage = hitPlayer(playerHealth)
      playerHealth = playerHealth - damage
      time.sleep(1)
      print("You have " + str(playerHealth) + " remaining")
      time.sleep(1)
  whoWins(playerHealth, bossHealth)

def hack():
    compcode = "raddoc2020"
    print("find the computer password")
    print("rldk-akjg-dnjj")
    print("dmf-ocn-cmf")
    print("245-014-249-034")
    print("Input Password")
    pas = input()
    while pas != compcode:
        print("try again")
    else:
        print("Correct")
    
def main():
    location = 200
    print("Hospital Escape")
    print("by: Christian, Megan, Abood")
    print("You have just gotton in a car crash and when you wake up in the hospital, but there is no elese there.")
    time.sleep(1)
    while True:
        print(roomArray[location])
        print("please type: n, s, e, w, or quit")
        userinput = input()
        location =  move(userinput, location)
        if itemArray[location] != False:
            print("there is an item here:" + itemArray[location])
            pickUpItem()

