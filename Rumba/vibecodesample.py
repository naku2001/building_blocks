
dirtX = 5  # Random X location for dirt
dirtY = 7  # Random Y location for dirt

# Variables (Simple variables only)
posX = 0
posY = 0
direction = 1 # 1 = moving right, -1 = moving left
dirtFound = False

print("Roomba begins.")
print(f"Starting position: ({posX}, {posY})")

# Search Algorithm (Snaking Pattern)
while not dirtFound:
    # Check for dirt at current location
    if posX == dirtX and posY == dirtY:
        print("The Roomba successfully cleans up the pile of dirt.")
        dirtFound = True
    else:
        # Move logic
        # If moving right and not at right wall
        if direction == 1 and posX < 9:
            posX += 1
        # If moving left and not at left wall
        elif direction == -1 and posX > 0:
            posX -= 1
        # If at a wall, move down to next row and flip direction
        else:
            if posY < 9:
                posY += 1
                direction *= -1
            else:
                # This handles the case where the whole room is searched
                break
        
        print(f"Entering new location: ({posX}, {posY})")

# Return to Dock Algorithm
while posX != 0 or posY != 0:
    if posX > 0:
        posX -= 1
    elif posY > 0:
        posY -= 1
        
    print(f"Returning to dock: ({posX}, {posY})")

print("Roomba arrives back at the docking station.")