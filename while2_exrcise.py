

while True:

    command = input ("Insert command")
    command = command.title()

    if command == "Start":
        print ("Engine is on!")

    elif command == "Stop":
        print ("Engine is off!")

    elif command == "Help":
        print ("The availble commands are Start and Stop")

    elif command == "Exit":
        print ("End")
        break

    else:
        print ("Unknown command!")
