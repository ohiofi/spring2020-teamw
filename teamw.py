roomArray = []
itemArray = []
import time
for i in range(999):
  roomArray.append(False)
  itemArray.append(False)

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

itemArray[201] = "Pill bottle"
itemArray[300] = "Phone"
itemArray[400] = "coins"
itemArray[602] = "Keycard"
itemArray[403] = "Syringe"
itemArray[603] = "Battery"

def main():
    location = 0
    print("Hospital Escape")
    print("by: Christian, Megan, Abood")
    time.sleep(1)
    while True:
        print(roomArray[location])
        print("please type: n, s, e, w, or quit")
        userinput = input()
        move(userinput, location)
        location = move()

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

