roomArray = []
itemArray = []
for i in range(999):
  roomArray.append(False)
  itemArray.append(False)

roomArray[200] = "You are in the corner of a room with walls to the north and west of you. Further east in room is a chair, and to the south west there is a tiny window"
roomArray[400] = "you are near a chair and the walls of the room are to the north and east of you. You can see a tiny window to the south west and a door to the far south"
roomArray[301]= "there is a tiny window letting very little light in and there is door to the far east"
roomArray[300] = "there is a wall to the north of you. There is alos a chair the the west, a vhair to the east and a tiny window to the south"
roomArray[201]= "there is walls to both the west and east of you. There is nothing but a tiny window to the east and a bed to the north in this room."
roomArray[401]= "there is a door directly to the east to leave this room. There is also a chair to the north and a tiny window to the west."


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
        if RoomArray[roomNumber] == False:
            print ("You can't go there")
            return False
        else: 
            return True
    except:
        print ("You can't go there")
        return False
    
