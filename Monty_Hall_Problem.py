import random
import pyinputplus


def input_mode():
    print("Would you like to play in Interactive or Batch mode?\n")
    mode = pyinputplus.inputMenu(['Interactive', 'Batch'], numbered=True)
    return mode


def input_playcount():
    playcount = pyinputplus.inputInt("How many times would you like to run the"
                                     " simulation?\n")
    return playcount


def input_choosedoor(chosen_doors):
    doorchoice = pyinputplus.inputInt("Do you think the grand prize is behind "
                                      "door #1, door #2, or door #3?\n")
    chosen_doors.append(doorchoice)
    return chosen_doors


def input_offerswitch(chosen_doors, switchto_doors, playcount, mode):
    switch = ""
    if mode == "Interactive":
            for rep in range(0, playcount):
                print("Ok, you chose door #" + str(chosen_doors[rep]) + ".\n"
                      "\nI can tell you that the grand prize is either behind "
                      "door #" + str(chosen_doors[rep]) + ", or behind door "
                      "#" + str(switchto_doors[rep]) + ".\n")
                print("So, would you like to keep your original door, or would"
                      " you like to switch to door #" +
                      str(switchto_doors[rep]))
                keeporswitch = pyinputplus.inputMenu(['Keep Original',
                                                      'Switch Doors'],
                                                     numbered=True)
                if keeporswitch == "Keep Original":
                    switch = "N"
                elif keeporswitch == "Switch Doors":
                    switch = "Y"
    elif mode == "Batch":
        print("Ok, I will run the simulation", playcount, "times.\n"
              "\nDo you want me to keep the originally picked door, or switch "
              "to the offered door?")
        keeporswitch = pyinputplus.inputMenu(['Keep Original', 'Switch Doors'],
                                             numbered=True)
        if keeporswitch == "Keep Original":
            switch = "N"
        elif keeporswitch == "Switch Doors":
            switch = "Y"
    return switch


def process_playgame(mode):
    winning_doors = []
    chosen_doors = []
    switchto_doors = []
    finalchoice_doors = []
    didiwin = []
    switch = ""
    if mode == "Interactive":
        playcount = 1
        input_choosedoor(chosen_doors)
    elif mode == "Batch":
        playcount = input_playcount()
        process_generatedoors(playcount, chosen_doors)
    process_generatedoors(playcount, winning_doors)
    process_switchtodoors(winning_doors, chosen_doors, playcount,
                          switchto_doors)
    switch = input_offerswitch(chosen_doors, switchto_doors, playcount, mode)
    process_finalchoicedoors(chosen_doors, switchto_doors, switch,
                             finalchoice_doors, playcount)
    process_didiwin(playcount, finalchoice_doors, winning_doors, didiwin)
    output_results(mode, didiwin, playcount)
    return


def process_generatedoors(playcount, random_doors):
    for reps in range(0, playcount):
        random_doors.append(random.randint(1, 3))
    return random_doors


def process_switchtodoors(winning_doors, chosen_doors, playcount,
                          switchto_doors):
    for rep in range(0, playcount):
        if chosen_doors[rep] == winning_doors[rep]:
            switchto_doors.append(((chosen_doors[rep] +
                                   random.randint(0, 1)) % 3) + 1)
        else:
            switchto_doors.append(winning_doors[rep])
    return switchto_doors


def process_finalchoicedoors(chosen_doors, switchto_doors, switch,
                             finalchoice_doors, playcount):
    for reps in range(0, playcount):
        if switch == "Y":
            finalchoice_doors.append(switchto_doors[reps])
        elif switch == "N":
            finalchoice_doors.append(chosen_doors[reps])
        else:
            print("Something has gone disastrously wrong!")
            exit(98)
    return finalchoice_doors


def process_didiwin(playcount, finalchoice_doors, winning_doors, didiwin):
    for reps in range(0, playcount):
        if finalchoice_doors[reps] == winning_doors[reps]:
            didiwin.append("Y")
        else:
            didiwin.append("N")
    return didiwin


def output_welcome():
    print("\nLET'S MAKE A DEAL!")
    print("\nWe're going to simulate what is commonly known as the "
          "'Monty Hall Problem.'\n")
    return


def output_results(mode, didiwin, playcount):
    wins = 0
    for rep in range(0, playcount):
        if didiwin[rep] == "Y":
            wins = wins + 1
    if mode == "Batch":
        print("You played", playcount, "games.  Of those, you won", wins, "games.")
        print("\nThat's good for a win percentage of " +
              str(round(wins/playcount * 100, 1)) + "%")
    else:
        if wins == 0:
            print("I'm sorry, you didn't win this time.  Thanks for playing.")
        else: print("Congratulations, you won!")
    return


def main():
    output_welcome()
    mode = input_mode()
    process_playgame(mode)


main()
