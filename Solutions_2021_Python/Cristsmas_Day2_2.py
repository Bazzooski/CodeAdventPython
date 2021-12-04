def ReadFile(Filepath):
    with open(Filepath) as f:
        Lines = f.read().splitlines()
    return Lines

horizontal_position = 0
vertical_position = 0
aim = 0

def update_position(MovementString):
    Movement = MovementString.split(" ")
    global horizontal_position
    global vertical_position
    global aim
    if(Movement[0] == "forward"):
        horizontal_position += int(Movement[1])
        vertical_position += aim*int(Movement[1])
    if(Movement[0] == "down"):
        aim += int(Movement[1])
    if(Movement[0] == "up"):
        aim -= int(Movement[1])

def Main():
    log_lines = ReadFile('D:\Tools\input_Day2.txt')
    for line in log_lines:
        update_position(line)
    print("Horizontal Position: " + str(horizontal_position) + "\nVertical Position: " + str(vertical_position) + "\nTotal Answer: "+ str(vertical_position*horizontal_position))

Main()

