#####################################################
############                           ##############
###               Meiro : Get out!                ###
############                           ##############
#####################################################
#                       Copyright: Leo Largillet 2021



# Dependencies

import os
import random
import time
import sys
import pickle

# General functions

def clear() :
    os.system("clear")

# Prints blank quantity times

def printVoid(quantity) :
    i = 0
    while i < quantity :
        print("")
        i = i + 1

# Displays message progressively

def progressiveDisplay(message) :
    for char in message :
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)

# Adds Bold or underline to text

def textFx(fx, text_to_fx) :
    fx_markup = ""
    if fx == "bold" :
        fx_markup = "\033[1m"
    elif fx == "underline" :
        fx_markup = "\033[4m"
    fx_txt = fx_markup + text_to_fx + "\033[0m"

    return fx_txt

# Adds color to text

def textColor(color, text_to_color) :
    color_list = [{"red": "\033[31;1m",
                   "blue": "\033[36;1m",
                   "green": "\033[32;1m",
                   "grey": "\033[37m",
                   "darkgrey": "\033[90m"}]
    colored_color = color_list[0][color]
    colored_txt = colored_color + text_to_color + "\033[0m"

    return colored_txt

# Waits for the user to press enter key

def pressEnter(message) :
    for char in message :
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)
    raw_input()

# Allows to avoid bugs with user pressing space bar while not asked

def selectOption(text, fnct) :
    progressiveDisplay(text)
    print("")
    choice = 0

    while True:
        try:
            choice = int(raw_input("> "))
        except ValueError :
            eval(fnct)
            progressiveDisplay("> Please provide a valid answer.")
            print("")
            continue
        else : 
            break
    return choice

# Same thing but when asking for a str reply

def enterChoice(text, fnct) :
    progressiveDisplay(text)
    print("")
    choice = ""

    while True:
        try:
            choice = str(raw_input("> "))
        except ValueError :
            eval(fnct)
            progressiveDisplay("> Please provide a valid answer.")
            print("")
            continue
        else : 
            break
    return choice

# Interface

def header() :
    print(textColor("grey","|/+----===-[          ")+textFx("bold","Meiro : Get Out!")+textColor("grey","          ]-===----+\|"))
    print(textColor("grey","|") + textColor("green","  [ |||||||||||||||||||||||||||||||||||||||||||||||||| ]  ") + textColor("grey","|"))
    print(textColor("grey","|\+--=========---() > ---==<-==->==--- < ()---=========--+/|"))

def footer(text) :
    print(textColor("grey","|\+--=========---() > ---==<-==->==--- < ()---=========--+/|"))
    print(textColor("grey","|") + textColor("green","  [ ||||||||||||| [ ") + textFx("bold", text) + textColor("green"," ] ||||||||||||| ]  ") + textColor("grey","|"))
    print(textColor("grey","|/+----=====---(}   > ---= <    > =--- <   {)---=====----+\|"))
    printVoid(1)

def headerGame() :
    print(textColor("grey","|/+----===-[          ")+textFx("bold","Meiro : Get Out!")+textColor("grey","          ]-===----+\|"))
    print(textColor("grey","|") + "  " + headerXp() + "  " + textColor("grey","|"))
    print(textColor("grey","|\+--=========---() > ---==<-==->==--- < ()---=========--+/|"))

def footerGame() :
    print(textColor("grey","|\+------===")+textColor("darkgrey","\-===-\--\->->>-<-->-<<-<-/--/-===-/")+textColor("grey","===------+/|"))
    print(textColor("darkgrey","| >->-") + footerMoney() + textColor("darkgrey",">-") + " [ " + footerName() + " ] " + textColor("darkgrey","-<") + footerHp() + textColor("darkgrey","-<-< |"))
    print(textColor("grey","|/+---==\----=--==/-<-<<   -<-->-   >>->-\==--=----/==---+\|"))
    printVoid(1)

def headerXp() :
    #[ Lv.01 ] [||||||||||||||||||||||||||||||||||||||    ] [      500 @ ] [ 100/100 HP ]
    lvl_to_display = ""
    bars_counter = (float(player["xp"]) / float(xp_required[player["level"]])) * 42
    bars_counter = int(bars_counter)
    bars_to_display = ""

    if player["level"] < 10 :
        lvl_to_display = "0" + str(player["level"])
    else :
        lvl_to_display = str(player["level"])

    i = 0
    while i < 42 :
        if i < bars_counter :
            bars_to_display = bars_to_display + textColor("blue","|")
        else :
            bars_to_display = bars_to_display + textColor("darkgrey","|")
        i = i + 1    

    return textColor("grey", "[ ") + textFx("bold", "Lv.") + textColor("blue",lvl_to_display) + textColor("grey", " ] [") + bars_to_display + textColor("grey", "]")

def footerMoney() :
    money_to_display = str(player["money"])
    if player["money"] < 10 :
        money_to_display = "  " + money_to_display
    elif player["money"] < 100 :
        money_to_display = " " + money_to_display
    return textColor("red", "[      " + money_to_display + " @ ]")

def footerHp() :
    hp_to_display = str(player["hp"])
    if hp_to_display < 10 :
        hp_to_display = "  " + hp_to_display
    elif hp_to_display < 100 :
        hp_to_display = " " + hp_to_display

    return textColor("green", "[ " + hp_to_display + "/" + str(player["hp_max"]) + " HP ]")

# Allows to se the usernam in the middle in function of its length

def footerName() :
    if len(player["name"]) == 2 :
        return textFx("bold", "    " + player["name"] + "    ")
    elif len(player["name"]) == 3 :
        return textFx("bold", "   " + player["name"] + "    ")
    elif len(player["name"]) == 4 :
        return textFx("bold", "   " + player["name"] + "   ")
    elif len(player["name"]) == 5 :
        return textFx("bold", "  " + player["name"] + "   ")
    elif len(player["name"]) == 6 :
        return textFx("bold", "  " + player["name"] + "  ")
    elif len(player["name"]) == 7 :
        return textFx("bold", " " + player["name"] + "  ")
    elif len(player["name"]) == 8 :
        return textFx("bold", " " + player["name"] + " ")
    elif len(player["name"]) == 9 :
        return textFx("bold", "" + player["name"] + " ")
    elif len(player["name"]) == 10 :
        return textFx("bold", "" + player["name"] + "")

# Launch animation

def launchAnimation(text, sub) :
    clear()
    header()

    printVoid(6)
    print(">                     "+ text)
    printVoid(1)
    print(">                     " + sub)
    printVoid(6)

    footer("   Press Start!   ")

def launch(gotomenu) :

    launchAnimation("       --       ","")
    time.sleep(0.05)

    launchAnimation("      ----      ","")
    time.sleep(0.05)

    launchAnimation("     ------     ","")
    time.sleep(0.05)

    launchAnimation("   ----------   ","")
    time.sleep(0.05)

    launchAnimation(" -------------- ","")
    time.sleep(0.05)

    launchAnimation("----------------","")
    time.sleep(0.05)

    launchAnimation("z--Xe < jie izo%","")
    time.sleep(0.05)

    launchAnimation("FL-cd r r e zz !","")
    time.sleep(0.05)

    launchAnimation("2MFls ; Kzk ola-","")
    time.sleep(0.05)

    launchAnimation("41L6d k Mas lap+","")
    time.sleep(0.05)

    launchAnimation("V1Krz ; Avo Oke&","")
    time.sleep(0.05)

    launchAnimation("Mfzgo : EJi koA0","")
    time.sleep(0.05)

    launchAnimation("Meiro : Get Out!","")
    time.sleep(1)

    launchAnimation("Meiro : Get Out!","       []       ")
    time.sleep(0.05)

    launchAnimation("Meiro : Get Out!","     [----]     ")
    time.sleep(0.05)

    launchAnimation("Meiro : Get Out!","   [--------]   ")
    time.sleep(0.05)

    launchAnimation("Meiro : Get Out!"," [------------] ")
    time.sleep(0.05)

    launchAnimation("Meiro : Get Out!","[--------------]")
    time.sleep(0.05)

    launchAnimation("Meiro : Get Out!","----------------")
    time.sleep(0.5)

    pressEnter("> Press Enter to begin...")

    if gotomenu == True :
        mainMenu("> Enter your choice right below.")

# Credits

def gameCredits() :
    clear()
    header()
    printVoid(15)
    footer("     Credits      ")

    time.sleep(0.6)

    clear()
    header()
    printVoid(14)
    print("                    An original game by:                    ")
    footer("     Credits      ")

    time.sleep(0.3)

    clear()
    header()
    printVoid(13)
    print("                    An original game by:                    ")
    print("                       Leo Largillet                        ")
    footer("     Credits      ")

    time.sleep(0.3)

    clear()
    header()
    printVoid(12)
    print("                    An original game by:                    ")
    print("                       Leo Largillet                        ")
    printVoid(1)
    footer("     Credits      ")

    time.sleep(0.3)

    clear()
    header()
    printVoid(11)
    print("                    An original game by:                    ")
    print("                       Leo Largillet                        ")
    printVoid(2)
    footer("     Credits      ")

    time.sleep(0.3)

    clear()
    header()
    printVoid(10)
    print("                    An original game by:                    ")
    print("                       Leo Largillet                        ")
    printVoid(3)
    footer("     Credits      ")

    time.sleep(0.3)

    clear()
    header()
    printVoid(9)
    print("                    An original game by:                    ")
    print("                       Leo Largillet                        ")
    printVoid(4)
    footer("     Credits      ")

    time.sleep(0.3)

    clear()
    header()
    printVoid(8)
    print("                    An original game by:                    ")
    print("                       Leo Largillet                        ")
    printVoid(5)
    footer("     Credits      ")

    time.sleep(0.3)

    clear()
    header()
    printVoid(7)
    print("                    An original game by:                    ")
    print("                       Leo Largillet                        ")
    printVoid(5)
    print("    Interface design: Leo Largillet                         ")
    footer("     Credits      ")

    time.sleep(0.3)

    clear()
    header()
    printVoid(6)
    print("                    An original game by:                    ")
    print("                       Leo Largillet                        ")
    printVoid(5)
    print("    Interface design: Leo Largillet                         ")
    printVoid(1)
    footer("     Credits      ")

    time.sleep(0.3)

    clear()
    header()
    printVoid(5)
    print("                    An original game by:                    ")
    print("                       Leo Largillet                        ")
    printVoid(5)
    print("    Interface design: Leo Largillet                         ")
    printVoid(1)
    print("    Game development: Leo Largillet                         ")
    footer("     Credits      ")

    time.sleep(0.3)

    clear()
    header()
    printVoid(4)
    print("                    An original game by:                    ")
    print("                       Leo Largillet                        ")
    printVoid(5)
    print("    Interface design: Leo Largillet                         ")
    printVoid(1)
    print("    Game development: Leo Largillet                         ")
    printVoid(1)
    footer("     Credits      ")

    time.sleep(0.3)

    clear()
    header()
    printVoid(3)
    print("                    An original game by:                    ")
    print("                       Leo Largillet                        ")
    printVoid(5)
    print("    Interface design: Leo Largillet                         ")
    printVoid(1)
    print("    Game development: Leo Largillet                         ")
    printVoid(1)
    print("    Original idea: Leo Largillet                         ")
    footer("     Credits      ")

    time.sleep(0.3)

    clear()
    header()
    printVoid(2)
    print("                    An original game by:                    ")
    print("                       Leo Largillet                        ")
    printVoid(5)
    print("    Interface design: Leo Largillet                         ")
    printVoid(1)
    print("    Game development: Leo Largillet                         ")
    printVoid(1)
    print("    Original idea: Leo Largillet                         ")
    printVoid(1)
    footer("     Credits      ")

    time.sleep(0.3)

    clear()
    header()
    printVoid(1)
    print("                    An original game by:                    ")
    print("                       Leo Largillet                        ")
    printVoid(5)
    print("    Interface design: Leo Largillet                         ")
    printVoid(1)
    print("    Game development: Leo Largillet                         ")
    printVoid(1)
    print("    Original idea: Leo Largillet                         ")
    printVoid(2)
    footer("     Credits      ")

    time.sleep(0.3)

    clear()
    header()
    print("                    An original game by:                    ")
    print("                       Leo Largillet                        ")
    printVoid(5)
    print("    Interface design: Leo Largillet                         ")
    printVoid(1)
    print("    Game development: Leo Largillet                         ")
    printVoid(1)
    print("    Original idea: Leo Largillet                         ")
    printVoid(3)
    footer("     Credits      ")

    time.sleep(0.3)

    clear()
    header()
    print("                       Leo Largillet                        ")
    printVoid(5)
    print("    Interface design: Leo Largillet                         ")
    printVoid(1)
    print("    Game development: Leo Largillet                         ")
    printVoid(1)
    print("    Original idea: Leo Largillet                         ")
    printVoid(4)
    footer("     Credits      ")

    time.sleep(0.3)

    clear()
    header()
    printVoid(5)
    print("    Interface design: Leo Largillet                         ")
    printVoid(1)
    print("    Game development: Leo Largillet                         ")
    printVoid(1)
    print("    Original idea: Leo Largillet                         ")
    printVoid(5)
    footer("     Credits      ")

    time.sleep(0.75)

    clear()
    header()
    printVoid(15)
    footer("     Credits      ")

    time.sleep(0.2)

    clear()
    header()
    printVoid(7)
    print("                    Thanks for playing!                     ")
    printVoid(7)
    footer("     Credits      ")

    time.sleep(0.2)

    clear()
    header()
    printVoid(7)
    print("                    Thanks for playing!                     ")
    printVoid(7)
    footer("     Credits      ")

    time.sleep(3)

    launch(True)

# Menu navigation

def displayMenu() :
    clear()
    header()

    printVoid(4)
    print(">     1 : New game")
    printVoid(1)
    print(">     2 : Load game")
    printVoid(1)
    print(">     3 : Credits")
    printVoid(1)
    print(">     4 : Exit")
    printVoid(4)

    footer("    Main  menu    ")

# First menu

def mainMenu(text) :

    displayMenu()
    choice = selectOption(text, "displayMenu()")

    if choice != 1 and choice != 2 and choice != 3 and choice != 4 :
        mainMenu("> Please enter a valid number.")

    elif choice == 1 :
        displayMenu()
        progressiveDisplay("> Initializing...")
        time.sleep(0.75)
        initGame()

    elif choice == 2 :
        displayMenu()
        progressiveDisplay("> Looking for existing save...")
        time.sleep(0.75)
        gameLoad("> Enter your choice right below.")

    elif choice == 3 :
        displayMenu()
        progressiveDisplay("> Loading credits...")
        gameCredits()

    elif choice == 4 :
        displayMenu()
        progressiveDisplay("> Quitting...")
        time.sleep(0.75)
        printVoid(2)

# Used to develop the game and check if the map works

def checkMove(latitude,longitude) :
    longitude = longitude - 1
    print(map_stage_1[latitude][longitude]["value"])

    if map_stage_1[latitude + 1][longitude]["value"] == 2 :
        print("no wall")

# Init of a new game

def initGame() :
    isPlace = False

    if not os.path.isfile('save_1.dat') :
        current_save = 1
        isPlace = True
        narration("This game will be saved on Save 1.","","")
    elif not os.path.isfile('save_2.dat') :
        current_save = 2
        isPlace = True
        narration("This game will be saved on Save 2.",textColor("darkgrey","Save 1 was already occupied."),"")
    elif not os.path.isfile('save_3.dat') :
        current_save = 3
        isPlace = True
        narration("This game will be saved on Save 3.",textColor("darkgrey","Save 1 and Save 2 were already occupied."),"")
    else :
        narration("You already have 3 saves registered.",textColor("darkgrey","Fix: you can delete a save file from the main folder."),"")
        mainMenu("> Enter your choice right below.")

    if isPlace == True :
        
        askName("> Write your name below.")

        narration("Welcome to the game, " + textColor("blue", player["name"] + "!"),"","")

        gameSave(current_save)

        introduction()

        tutorial()

        displayMap(True, "You are the " + textColor("red","[ x ]") + ". Press Enter to continue...")

        game("> Enter your choice right below.")

# Ask for player's name

def displayAskName() :
    clear()
    header()

    printVoid(7)
    print(">                    What is your name?                     ")
    printVoid(7)

    footer("    Your  name    ")


def askName(text) :
    displayAskName()
    choice = enterChoice(text, "displayAskName()")

    if len(choice) > 10 or len(choice) < 2 :
        askName("> Please enter a valid name (2-10 char.).")
    else :
        player["name"] = choice

# Quick introduction and tutorial

def introduction() :
    narration("Birds are singing. Or are they birds?","At least, they are the only quite familiar","thing around you this morning.")
    narration("It seems like you woke up far away from home.","Or did you wake up?","It is not your room facing you, it's a giant maze.")
    narration("Anyways, dream or not, you'll be better out.",textColor("darkgrey","Is that a growl I heard?!"),"")
    launch(False)

def tutorial() :
    narration("This is a short " + textColor("blue","tutorial ") + "to help you begin your", "journey in Meiro: Get out!",textColor("darkgrey","Let's go through the basics."))
    narration("You can navigate by entering the " + textColor("blue","corresponding key,"),"with that, you will be able to control your character","and therefore search for the " + textColor("green","exit") + " of this maze.")
    narration("The game is built around a powerful interactive map,", "you can access it in your inventory. " + textColor("red"," [ x ] : You"), textColor("blue","[ * ] : Camp") + "     " + textColor("grey","[ + ] : Explored") + "     " + textColor("red","///// : Walls"))
    narration("It is possible to save the game with up to " + textColor("blue","3 saves."),"To do so, you must be in a " + textColor("blue","Camp [ * ]") + ", then open", textColor("red","[ 7: Options ]") + " and select " + textColor("blue","Save") + " or " + textColor("blue","Save & quit") + ".")
    narration("Finally, when moving to new " + textColor("blue","tiles") + ", you might encounter", textColor("red","mighty monsters") + " or find " + textColor("green","new items") + ", so be sure to","get prepared perfectly to fight them and buy " + textColor("blue","weapons") + "!")
    narration("That's it for our " + textColor("blue","tutorial") + ", enjoy playing Meiro!",textColor("darkgrey","You can replay this tutorial in [7: Options]."),"")


# Load an existing game file

def displayLoadMenu() :
    clear()
    header()

    printVoid(4)
    print(">     1 : Load save 1")
    printVoid(1)
    print(">     2 : Load save 2")
    printVoid(1)
    print(">     3 : Load save 3")
    printVoid(1)
    print(">     4 : Back to menu")
    printVoid(4)

    footer("    Load  save    ")

# Load an existing game

def gameLoad(text) :

    displayLoadMenu()
    choice = selectOption(text, "displayLoadMenu()")

    if choice != 1 and choice != 2 and choice != 3 and choice != 4 :
        mainMenu("> Please enter a valid number.")

    elif choice == 1 :
        displayLoadMenu()
        progressiveDisplay("> Searching for a file...")
        printVoid(1)
        time.sleep(0.5)
        if os.path.isfile('save_1.dat') :
            chargeSave(1)
        else :
            gameLoad("> No save was found, try something else.")

    elif choice == 2 :
        displayLoadMenu()
        progressiveDisplay("> Searching for a file...")
        printVoid(1)
        time.sleep(0.5)
        if os.path.isfile('save_2.dat') :
            chargeSave(2)
        else :
            gameLoad("> No save was found, try something else.")

    elif choice == 3 :
        displayLoadMenu()
        progressiveDisplay("> Searching for a file...")
        printVoid(1)
        time.sleep(0.5)
        if os.path.isfile('save_3.dat') :
            chargeSave(3)
        else :
            gameLoad("> No save was found, try something else.")

    elif choice == 4 :
        displayLoadMenu()
        progressiveDisplay("> Loading menu...")
        time.sleep(0.25)
        mainMenu("> Enter your choice right below.")

# Interactions

def narration(text1, text2, text3) :
    clear()
    header()

    printVoid(6)
    print(">     " + text1)
    print("      " + text2)
    print("      " + text3)
    printVoid(6)

    footer("   Information    ")
    pressEnter("> Press Enter to continue...")

def narrationGame(text1, text2, text3) :
    clear()
    headerGame()

    printVoid(6)
    print(">     " + text1)
    print("      " + text2)
    print("      " + text3)
    printVoid(6)

    footerGame()
    pressEnter("> Press Enter to continue...")

# Interactive map generated from an array

def mapPoint(stage, latitude, longitude) :
    point_to_return = ""
    if stage[latitude][longitude]["value"] == 3 and stage[latitude][longitude]["visited"] == False :
        point_to_return = textColor("grey","[ . ]")
    elif stage[latitude][longitude]["value"] == 3 and stage[latitude][longitude]["visited"] == True :
        point_to_return = textColor("blue","[ * ]")
    elif stage[latitude][longitude]["value"] == 2 and stage[latitude][longitude]["visited"] == True :
        point_to_return = textColor("darkgrey","[ + ]")
    elif stage[latitude][longitude]["value"] == 2 and stage[latitude][longitude]["visited"] == False :
        point_to_return = textColor("grey","[ . ]")
    
    if latitude == player["latitude"] and longitude + 1 == player["longitude"]:
        point_to_return = textColor("red","[ x ]")

    return point_to_return

def displayMap(show, text) :
    clear()
    header()
    printVoid(1)

    i = 1

    while i < len(map_stage_1) :
        line = "   "
        post_line = "   "
        j = 0

        while j < len(map_stage_1[i]) :
            block_content = ""
            post_block_content = ""

            if j == 0 :
                if map_stage_1[i][j]["value"] == 1 :
                    block_content = block_content + textColor("red","//////")
                    post_block_content = post_block_content + textColor("red","//////")
                elif map_stage_1[i][j]["value"] == 2 :
                    if map_stage_1[i][j+1]["value"] == 2 or map_stage_1[i][j+1]["value"] == 3 :
                        block_content = block_content + mapPoint(map_stage_1, i, j) + "-"
                    else :
                        block_content = block_content + mapPoint(map_stage_1, i, j) + " "
                    if i < 7 :
                        if map_stage_1[i+1][j]["value"] == 2 or map_stage_1[i+1][j]["value"] == 3 :
                            post_block_content = post_block_content + "  |   "
                        else :
                            post_block_content = post_block_content + textColor("red","//////")
                elif map_stage_1[i][j]["value"] == 3 :
                    if map_stage_1[i][j+1]["value"] == 2 or map_stage_1[i][j+1]["value"] == 3 :
                        block_content = block_content + mapPoint(map_stage_1, i, j) + "-"
                    else :
                        block_content = block_content + mapPoint(map_stage_1, i, j) + " "
                    if i < 7 :
                        if map_stage_1[i+1][j]["value"] == 2 or map_stage_1[i+1][j]["value"] == 3 :
                            post_block_content = post_block_content + "  |   "
                        else :
                            post_block_content = post_block_content + textColor("red","//////")

                if map_question_marks == True :
                    if i == 1 :
                        if map_stage_1[i][j+1]["visited"] == True or map_stage_1[i+1][j+1]["visited"] == True or map_stage_1[i+1][j]["visited"] == True :
                            nothinghappens = "nothing"
                        elif map_stage_1[i][j]["visited"] == False :
                            block_content = textColor("darkgrey", "??????")
                            post_block_content = textColor("darkgrey", "??????")
                    
                    elif i == 7 :
                        if map_stage_1[i][j+1]["visited"] == True or map_stage_1[i-1][j+1]["visited"] == True or map_stage_1[i-1][j]["visited"] == True :
                            nothinghappens = "nothing"
                        elif map_stage_1[i][j]["visited"] == False :
                            block_content = textColor("darkgrey", "??????")
                            post_block_content = textColor("darkgrey", "??????")
                    
                    else :
                        if map_stage_1[i][j+1]["visited"] == True or map_stage_1[i+1][j+1]["visited"] == True or map_stage_1[i+1][j]["visited"] == True or map_stage_1[i-1][j]["visited"] == True or map_stage_1[i-1][j+1]["visited"] == True :
                            nothinghappens = "nothing"
                        elif map_stage_1[i][j]["visited"] == False :
                            block_content = textColor("darkgrey", "??????")
                            post_block_content = textColor("darkgrey", "??????")
                        


            elif j == 7 :
                if map_stage_1[i][j]["value"] == 1 :
                    block_content = block_content + textColor("red","//////")
                    post_block_content = post_block_content + textColor("red","//////")
                elif map_stage_1[i][j]["value"] == 2 :
                    if map_stage_1[i][j-1]["value"] == 2 or map_stage_1[i][j-1]["value"] == 3 :
                        block_content = block_content + "-" + mapPoint(map_stage_1, i, j)
                    else :
                        block_content = block_content + " " + mapPoint(map_stage_1, i, j)
                    if i < 7 :
                        if map_stage_1[i+1][j]["value"] == 2 or map_stage_1[i+1][j]["value"] == 3 :
                            post_block_content = post_block_content + "   |  "
                        else :
                            post_block_content = post_block_content + textColor("red","//////")
                elif map_stage_1[i][j]["value"] == 3 :
                    if map_stage_1[i][j-1]["value"] == 2 or map_stage_1[i][j-1]["value"] == 3 :
                        block_content = block_content + "-" + mapPoint(map_stage_1, i, j)
                    else :
                        block_content = block_content + " " + mapPoint(map_stage_1, i, j)
                    if i < 7 :
                        if map_stage_1[i+1][j]["value"] == 2 or map_stage_1[i+1][j]["value"] == 3 :
                            post_block_content = post_block_content + "   |  "
                        else :
                            post_block_content = post_block_content + textColor("red","//////")
                
                if map_question_marks == True :
                    if i == 1 :
                        if map_stage_1[i][j-1]["visited"] == True or map_stage_1[i+1][j-1]["visited"] == True or map_stage_1[i+1][j]["visited"] == True :
                            nothinghappens = "nothing"
                        elif map_stage_1[i][j]["visited"] == False :
                            block_content = textColor("darkgrey", "??????")
                            post_block_content = textColor("darkgrey", "??????")
                    
                    elif i == 7 :
                        if map_stage_1[i][j-1]["visited"] == True or map_stage_1[i-1][j-1]["visited"] == True or map_stage_1[i-1][j]["visited"] == True :
                            nothinghappens = "nothing"
                        elif map_stage_1[i][j]["visited"] == False :
                            block_content = textColor("darkgrey", "??????")
                            post_block_content = textColor("darkgrey", "??????")
                    
                    else :
                        if map_stage_1[i][j-1]["visited"] == True or map_stage_1[i+1][j-1]["visited"] == True or map_stage_1[i+1][j]["visited"] == True or map_stage_1[i-1][j]["visited"] == True or map_stage_1[i-1][j-1]["visited"] == True :
                            nothinghappens = "nothing"
                        elif map_stage_1[i][j]["visited"] == False :
                            block_content = textColor("darkgrey", "??????")
                            post_block_content = textColor("darkgrey", "??????")

            else :
                if map_stage_1[i][j]["value"] == 1 :
                    block_content = block_content + textColor("red","///////")
                    post_block_content = post_block_content + textColor("red","///////")
                elif map_stage_1[i][j]["value"] == 2 :
                    if map_stage_1[i][j-1]["value"] == 1 and map_stage_1[i][j+1]["value"] == 1 :
                        block_content = block_content + " " + mapPoint(map_stage_1, i, j) + " "
                    elif map_stage_1[i][j-1]["value"] == 1 :
                        block_content = block_content + " " + mapPoint(map_stage_1, i, j) + "-"
                    elif map_stage_1[i][j+1]["value"] == 1 :
                        block_content = block_content + "-" + mapPoint(map_stage_1, i, j) + " "
                    else :
                        block_content = block_content + "-" + mapPoint(map_stage_1, i, j) + "-"
                    if i < 7 :
                        if map_stage_1[i+1][j]["value"] == 2 or map_stage_1[i+1][j]["value"] == 3 :
                            post_block_content = post_block_content + "   |   "
                        else :
                            post_block_content = post_block_content + textColor("red","///////")
                elif map_stage_1[i][j]["value"] == 3 :
                    if map_stage_1[i][j-1]["value"] == 1 and map_stage_1[i][j+1]["value"] == 1 :
                        block_content = block_content + " " + mapPoint(map_stage_1, i, j) + " "
                    elif map_stage_1[i][j-1]["value"] == 1 :
                        block_content = block_content + " " + mapPoint(map_stage_1, i, j) + "-"
                    elif map_stage_1[i][j+1]["value"] == 1 :
                        block_content = block_content + "-" + mapPoint(map_stage_1, i, j) + "  "
                    else :
                        block_content = block_content + "-" + mapPoint(map_stage_1, i, j) + "-"
                    if i < 7 :
                        if map_stage_1[i+1][j]["value"] == 2 or map_stage_1[i+1][j]["value"] == 3 :
                            post_block_content = post_block_content + "   |   "
                        else :
                            post_block_content = post_block_content + textColor("red","///////")
                
                if map_question_marks == True :
                    if i == 1 :
                        if map_stage_1[i][j-1]["visited"] == True or map_stage_1[i+1][j-1]["visited"] == True or map_stage_1[i+1][j]["visited"] == True or map_stage_1[i+1][j+1]["visited"] == True or map_stage_1[i][j+1]["visited"] == True :
                            nothinghappens = "nothing"
                        elif map_stage_1[i][j]["visited"] == False :
                            block_content = textColor("darkgrey", "???????")
                            post_block_content = textColor("darkgrey", "???????")
                    
                    elif i == 7 :
                        if map_stage_1[i][j-1]["visited"] == True or map_stage_1[i-1][j-1]["visited"] == True or map_stage_1[i-1][j]["visited"] == True or map_stage_1[i-1][j+1]["visited"] == True or map_stage_1[i][j+1]["visited"] == True :
                            nothinghappens = "nothing"
                        elif map_stage_1[i][j]["visited"] == False :
                            block_content = textColor("darkgrey", "???????")
                            post_block_content = textColor("darkgrey", "???????")
                    
                    else :
                        if map_stage_1[i][j-1]["visited"] == True or map_stage_1[i-1][j-1]["visited"] == True or map_stage_1[i-1][j]["visited"] == True or map_stage_1[i-1][j+1]["visited"] == True or map_stage_1[i+1][j-1]["visited"] == True or map_stage_1[i+1][j]["visited"] == True or map_stage_1[i+1][j+1]["visited"] == True or map_stage_1[i][j+1]["visited"] == True :
                            nothinghappens = "nothing"
                        elif map_stage_1[i][j]["visited"] == False :
                            block_content = textColor("darkgrey", "???????")
                            post_block_content = textColor("darkgrey", "???????")

            line = line + block_content
            post_line = post_line + post_block_content

            j += 1
        
        line = line + "   "
        if i < 7 :
            post_line = post_line + "   "

        print line
        if i < 7 :
            print post_line

        i += 1
    
    printVoid(1)
    
    footer("    Global Map    ")

    if show == True :
        pressEnter(text)
    else :
        print("> Processing...")

# Variables

# 1 = wall, 2 = normal case, 3 = camp
# Markups(Longitude)                          A                                             B                                                  C                                                  D                                                  E                                             F                                               G                                           H
map_stage_1 = [[{"value": 1, "visited": False, "spawn": False}, {"value": 1, "visited": False, "spawn": False}, {"value": 2, "visited": False, "spawn": False}, {"value": 1, "visited": False, "spawn": False}, {"value": 1, "visited": False, "spawn": False}, {"value": 1, "visited": False, "spawn": False}, {"value": 1, "visited": False, "spawn": False}, {"value": 1, "visited": False, "spawn": False}], #0 (Not displayed)
               [{"value": 3, "visited": False, "spawn": True}, {"value": 1, "visited": False, "spawn": False}, {"value": 2, "visited": False, "spawn": True}, {"value": 1, "visited": False, "spawn": False}, {"value": 2, "visited": False, "spawn": True}, {"value": 2, "visited": False, "spawn": True}, {"value": 2, "visited": False, "spawn": True}, {"value": 3, "visited": False, "spawn": True}], #1
               [{"value": 2, "visited": False, "spawn": True}, {"value": 2, "visited": False, "spawn": True}, {"value": 2, "visited": False, "spawn": True}, {"value": 2, "visited": False, "spawn": True}, {"value": 2, "visited": False, "spawn": True}, {"value": 1, "visited": False, "spawn": False}, {"value": 1, "visited": False, "spawn": False}, {"value": 1, "visited": False, "spawn": False}], #2
               [{"value": 1, "visited": False, "spawn": False}, {"value": 2, "visited": False, "spawn": True}, {"value": 1, "visited": False, "spawn": False}, {"value": 1, "visited": False, "spawn": False}, {"value": 1, "visited": False, "spawn": False}, {"value": 1, "visited": False, "spawn": False}, {"value": 3, "visited": False, "spawn": True}, {"value": 1, "visited": False, "spawn": False}], #3
               [{"value": 3, "visited": False, "spawn": True}, {"value": 2, "visited": False, "spawn": True}, {"value": 2, "visited": False, "spawn": True}, {"value": 1, "visited": False, "spawn": False}, {"value": 2, "visited": False, "spawn": True}, {"value": 1, "visited": False, "spawn": False}, {"value": 2, "visited": False, "spawn": True}, {"value": 2, "visited": False, "spawn": True}], #4
               [{"value": 2, "visited": False, "spawn": True}, {"value": 1, "visited": False, "spawn": False}, {"value": 2, "visited": False, "spawn": True}, {"value": 1, "visited": False, "spawn": False}, {"value": 3, "visited": True, "spawn": False}, {"value": 1, "visited": False, "spawn": False}, {"value": 1, "visited": False, "spawn": False}, {"value": 2, "visited": False, "spawn": True}], #5
               [{"value": 2, "visited": False, "spawn": True}, {"value": 2, "visited": False, "spawn": True}, {"value": 2, "visited": False, "spawn": True}, {"value": 1, "visited": False, "spawn": False}, {"value": 2, "visited": False, "spawn": True}, {"value": 1, "visited": False, "spawn": False}, {"value": 2, "visited": False, "spawn": True}, {"value": 2, "visited": False, "spawn": True}], #6
               [{"value": 1, "visited": False, "spawn": False}, {"value": 1, "visited": False, "spawn": False}, {"value": 2, "visited": False, "spawn": True}, {"value": 2, "visited": False, "spawn": True}, {"value": 2, "visited": False, "spawn": True}, {"value": 2, "visited": False, "spawn": True}, {"value": 2, "visited": False, "spawn": True}, {"value": 1, "visited": False, "spawn": False}], #7
]

# First is for weapons, second is for boosters, third is for loots
items = [[{"name": "Fist", "dmg": 14, "possessed": True, "equiped": True, "price": 0}, {"name": "Shovel", "dmg": 22, "possessed": False, "equiped": False, "price": 40}, {"name": "Pickaxe", "dmg": 28, "possessed": False, "equiped": False, "price": 100}, {"name": "Axe", "dmg": 35, "possessed": False, "equiped": False, "price": 250}, {"name": "Sword", "dmg": 50, "possessed": False, "equiped": False, "price": 450}, {"name": "Katana", "dmg": 88, "possessed": False, "equiped": False, "price": 990}],

             [{"name": "Health potion I", "type": "battle", "effect": 25, "possessed": 3, "price": 5}, {"name": "Health potion II", "type": "battle", "effect": 50, "possessed": 0, "price": 10}, {"name": "Health potion III", "type": "battle", "effect": 100, "possessed": 1, "price": 20}, {"name": "Maximum Health booster I", "type": "booster", "effect": 10, "possessed": 0, "price": 150}, {"name": "Maximum Health booster II", "type": "booster", "effect": 25, "possessed": 0, "price": 300}],

             [{"name": "Rare skin", "value": 10, "possessed": 0}, {"name": "Iron chip", "value": 22, "possessed": 0}, {"name": "Golden bone", "value": 57, "possessed": 0}, ]
]

player = {"name" : "undefined", "xp" : 50, "level" : 1, "stage" : 1, "latitude" : 5, "longitude" : 5, "hp": 100, "hp_max": 100, "money": 25}
xp_required = [0, 300, 450, 550, 700, 1000, 1500, 2000, 2500, 3000, 4000, 5000, 6000, 7500, 9000, 10000, 12000, 15000, 17500, 20000]
map_question_marks = True
mobs = [{"name" : "Golem", "dmg" : 8, "hp" : 140}, {"name" : "Giant spider", "dmg" : 12, "hp" : 80}, {"name" : "Zombie", "dmg" : 10, "hp" : 100}, {"name" : "Giant Mammoth", "dmg" : 25, "hp" : 450}]

# Saving the game

current_save = 1

def gameSave(number) :
    if number == 1 :
        with open('save_1.dat', 'wb') as f:
            pickle.dump([map_stage_1, player, items], f, protocol=2)
    elif number == 2 :
        with open('save_2.dat', 'wb') as f:
            pickle.dump([map_stage_1, player, items], f, protocol=2)
    elif number == 3 :
        with open('save_3.dat', 'wb') as f:
            pickle.dump([map_stage_1, player, items], f, protocol=2)

def loadSave(number) :
    if number == 1 :
        with open('save_1.dat', 'rb') as f:
            x, y, z = pickle.load(f)

        global map_stage_1
        map_stage_1 = x
        
        global player
        player = y

        global items
        items = z
    elif number == 2 :
        with open('save_2.dat', 'rb') as f:
            x, y, z = pickle.load(f)

        global map_stage_1
        map_stage_1 = x
        
        global player
        player = y

        global items
        items = z
    elif number == 3 :
        with open('save_3.dat', 'rb') as f:
            x, y, z = pickle.load(f)

        global map_stage_1
        map_stage_1 = x
        
        global player
        player = y

        global items
        items = z


def chargeSave(number) :
    current_save = number
    loadSave(number)
    narration("Welcome back, " + textColor("blue",player["name"]) + "!",textColor("darkgrey","Here is where you stopped last time:"),"")
    displayMap(True, "> Press Enter to resume game...")

    game("> Enter your choice right below.")

# Playing the game

def displacePlayer(direction) :

    if direction == 1 :
        displayMap(True, "Press Enter to move to the north.")
        player["latitude"] = player["latitude"] - 1
        if map_stage_1[player["latitude"]][player["longitude"]-1]["visited"] == False :
            map_stage_1[player["latitude"]][player["longitude"]-1]["visited"] = True

    if direction == 2 :
        displayMap(True, "Press Enter to move to the east.")
        player["longitude"] = player["longitude"] + 1
        if map_stage_1[player["latitude"]][player["longitude"]-1]["visited"] == False :
            map_stage_1[player["latitude"]][player["longitude"]-1]["visited"] = True

    if direction == 3 :
        displayMap(True, "Press Enter to move to the south.")
        player["latitude"] = player["latitude"] + 1
        if map_stage_1[player["latitude"]][player["longitude"]-1]["visited"] == False :
            map_stage_1[player["latitude"]][player["longitude"]-1]["visited"] = True
    
    if direction == 4 :
        displayMap(True, "Press Enter to move to the west.")
        player["longitude"] = player["longitude"] - 1
        if map_stage_1[player["latitude"]][player["longitude"]-1]["visited"] == False :
            map_stage_1[player["latitude"]][player["longitude"]-1]["visited"] = True

    displayMap(False, "")
    time.sleep(1)
    enterTile()

def displayGameTexts(text, active) :
    if active == 1 :
        return textColor("darkgrey", text)
    if active == 2 :
        return text
    if active == 3 :
        return textColor("green", text)
    
def displayGame(north, east, south, west, inventory, camp, options) :
    clear()
    headerGame()

    printVoid(6)
    print(">                 Please select an action.                  ")
    printVoid(4)
    if player["latitude"] == 1 and player["longitude"] == 3 :
        print(displayGameTexts(textColor("blue","[1: Go North]"), north) + "   " + displayGameTexts("[2: Go East]", east) + "    " + displayGameTexts("[3: Go South]", south) + "   " + displayGameTexts("[4: Go West]", west))
    else :
        print(displayGameTexts("[1: Go North]", north) + "   " + displayGameTexts("[2: Go East]", east) + "    " + displayGameTexts("[3: Go South]", south) + "   " + displayGameTexts("[4: Go West]", west))
    printVoid(1)
    print(displayGameTexts("[5: Inventory]", inventory) + "      " + displayGameTexts("[6: Camp interactions]", camp) + "      " + displayGameTexts("[7: Options]", options))
    printVoid(1)

    footerGame()

def game(text) :

    enable_north = 1
    enable_east = 1
    enable_south = 1
    enable_west = 1
    enable_inventory = 2
    enable_camp = 1
    enable_options = 2

    while True :
        try:
            if map_stage_1[player["latitude"]-1][player["longitude"]-1]["value"] != 1 :
                enable_north = 2
            break
        except IndexError:
            break

    while True :
        try:
            if map_stage_1[player["latitude"]][player["longitude"]]["value"] != 1 :
                enable_east = 2
            break
        except IndexError:
            break

    while True :
        try:
            if map_stage_1[player["latitude"]+1][player["longitude"]-1]["value"] != 1 :
                enable_south = 2
            break
        except IndexError:
            break

    while True :
        try:
            if map_stage_1[player["latitude"]][player["longitude"]-2]["value"] != 1 :
                enable_west = 2
            break
        except IndexError:
            break

    while True :
        try:
            if map_stage_1[player["latitude"]][player["longitude"]-1]["value"] == 3 :
                enable_camp = 2
            break
        except IndexError:
            break

    displayGame(enable_north, enable_east, enable_south, enable_west, enable_inventory, enable_camp, enable_options)

    choice = selectOption(text, "displayGame(" + str(enable_north) + "," + str(enable_east) + "," + str(enable_south) + "," + str(enable_west) + "," + str(enable_inventory) + "," + str(enable_camp) + "," + str(enable_options) + ")")

    if choice != 1 and choice != 2 and choice != 3 and choice != 4 and choice != 5 and choice != 6 and choice != 7 :
        game("> It seems like we can't do that. Let's try something else.")

    elif choice == 1 and enable_north == 2:
        enable_north = 3
        displayGame(enable_north, enable_east, enable_south, enable_west, enable_inventory, enable_camp, enable_options)
        progressiveDisplay("> Moving to the north...")
        time.sleep(0.25)
        displacePlayer(1)

    elif choice == 2 and enable_east == 2:
        enable_east = 3
        displayGame(enable_north, enable_east, enable_south, enable_west, enable_inventory, enable_camp, enable_options)
        progressiveDisplay("> Moving to the east...")
        time.sleep(0.25)
        displacePlayer(2)  

    elif choice == 3 and enable_south == 2:
        enable_south = 3
        displayGame(enable_north, enable_east, enable_south, enable_west, enable_inventory, enable_camp, enable_options)
        progressiveDisplay("> Moving to the south...")
        time.sleep(0.25)
        displacePlayer(3)  

    elif choice == 4 and enable_west == 2:
        enable_west = 3
        displayGame(enable_north, enable_east, enable_south, enable_west, enable_inventory, enable_camp, enable_options)
        progressiveDisplay("> Moving to the west...")
        time.sleep(0.25)
        displacePlayer(4)  

    elif choice == 5 and enable_inventory == 2 :
        enable_inventory = 3
        displayGame(enable_north, enable_east, enable_south, enable_west, enable_inventory, enable_camp, enable_options)
        progressiveDisplay("> Loading your items...")
        time.sleep(0.25)
        inventory("> Enter your choice right below.")

    elif choice == 6 and enable_camp == 2 :
        enable_camp = 3
        displayGame(enable_north, enable_east, enable_south, enable_west, enable_inventory, enable_camp, enable_options)
        progressiveDisplay("> Loading the camp...")
        time.sleep(0.25)
        campInteractions("> Enter your choice right below.")

    elif choice == 7 and enable_options == 2 :
        enable_options = 3
        displayGame(enable_north, enable_east, enable_south, enable_west, enable_inventory, enable_camp, enable_options)
        progressiveDisplay("> Loading the options...")
        time.sleep(0.25)
        options("> Enter your choice right below.")

    else :
        game("> It seems like we can't go there. Let's try something else.")

def displayEncounter(canRun, mob) :
    clear()
    headerGame()
    printVoid(6)
    print(">       A " + mobs[mob]["name"] + " appears! What will you do ?...       ")
    printVoid(3)
    if canRun == True :
        print("             [ 1: Fight ]       [ 2: Run away ]             ")
    elif canRun == False :
        print("             [[1: Fight]       " + textColor("darkgrey","[2: Run away]") + "             ")
    printVoid(4)
    footerGame()

def randomEncounter(text) :

    mob_to_fight = 0

    if random.randint(0,100) < 33 :
        mob_to_fight = 0
    elif random.randint(0,100) < 33 :
        mob_to_fight = 1
    else :
        mob_to_fight = 2

    displayEncounter(True, mob_to_fight)
    choice = selectOption(text, "displayEncounter(True, " + str(mob_to_fight) + ")")

    if choice != 1 and choice != 2 :
        mainMenu("> Please enter a valid number.")

    elif choice == 1 :
        progressiveDisplay("> Entering battle mode...")
        time.sleep(0.5)
        debutBattle(mob_to_fight)

    elif choice == 2 :
        if random.randint(0,100) < 40 :
            narration("You successfully ran away!","","")
        else :
            narration("You weren't able to run away!","Entering battle mode...","")
            progressiveDisplay("> Entering battle mode...")
            time.sleep(0.5)
            debutBattle(mob_to_fight)

def foundItem() :
    narration("You noticed something was shining in the corner when","you arrived, you decide to take a closer look...","")

    if random.randint(0,400) < 1 :
        narrationGame(textColor("red", "Super rare! +125 XP"),"It was a Katana!","The item has been added to your inventory.")
        items[0][5]["possessed"] = True
        xp(125)
    elif random.randint(0,400) < 2 :
        narrationGame(textColor("red", "Super rare! +125 XP"),"It was a Maximum Health II Potion!","The item has been added to your inventory.")
        items[1][4]["possessed"] = items[1][4]["possessed"] + 1
        xp(125)
    elif random.randint(0,100) < 5 :
        narrationGame(textColor("blue", "Rare! +65 XP"),"It was a bag of 20 @!","The coins have been added to your wallet.")
        money(20)
        xp(65)
    elif random.randint(0,100) < 5 :
        narrationGame(textColor("blue", "Rare! +65 XP"),"It was a Health III Potion!","The item has been added to your inventory.")
        items[1][2]["possessed"] = items[1][2]["possessed"] + 1
        xp(65)
    elif random.randint(0,100) < 15 :
        narrationGame(textColor("green", "Uncommon! +35 XP"),"It was a pouch of 5 @!","The coins have been added to your wallet.")
        money(5)
        xp(35)
    elif random.randint(0,100) < 35 :
        narrationGame(textColor("green", "Uncommon! +35 XP"),"It was a Health I Potion!","The item has been added to your inventory.")
        items[1][0]["possessed"] = items[1][0]["possessed"] + 1
        xp(35)
    else :
        narrationGame(textColor("grey", "Nice! +15 XP"),"It was a @ coin!","The coin has been added to your wallet.")
        money(1)
        xp(15)

def enterTile() :
    if player["latitude"] == 0 and player["longitude"] == 3 :
        narrationGame("Look over there! It looks like you found the "+textColor("blue","exit")+"!","However, a "+textColor("red","mighty Mammoth")+" was waiting for you!","In order for you to get out, you must bypass him!")
        debutBattle(3)
        gameCredits()
        sys.exit()
    else :
        if map_stage_1[player["latitude"]][player["longitude"] - 1]["spawn"] == True :
            if map_stage_1[player["latitude"]][player["longitude"] - 1]["value"] == 2 :
                if random.randint(0,100) < 45 :
                    randomEncounter("> Enter your choice right below.")
            elif map_stage_1[player["latitude"]][player["longitude"] - 1]["value"] == 3 :
                if random.randint(0,100) < 25 :
                    randomEncounter("> Enter your choice right below.")
        
        if map_stage_1[player["latitude"]][player["longitude"] - 1]["value"] == 2 :
            if random.randint(0,100) < 25 :
                foundItem()
        elif map_stage_1[player["latitude"]][player["longitude"] - 1]["value"] == 3 :
            if random.randint(0,100) < 10 :
                foundItem()

        if map_stage_1[player["latitude"]][player["longitude"] - 1]["value"] == 3 :
            narration("You arrived to a camp.", "Here, you will be able to recover your", "health, to save the game or to trade.") 

        game("> Enter your choice right below.")

def xp(quantity) :
    player["xp"] = player["xp"] + quantity
    if player["xp"] > xp_required[player["level"]] :
        xp_temp = player["xp"] - xp_required[player["level"]]
        player["xp"] = 0
        player["level"] = player["level"] + 1
        narrationGame("You earned " + str(quantity) + "XP !", "Congratulations, you are now level " + str(player["level"]) + "!", "")
        xp(xp_temp)
    else :
        narrationGame("You earned " + str(quantity) + "XP !", "", "")

def money(quantity) :
    player["money"] = player["money"] + quantity
    if player["money"] > 999 :
        player["money"] = 999
    narrationGame("You earned " + str(quantity) + "@ !", "", "")

def hp(effect, quantity) :
    if effect == 1 :
        player["hp"] = player["hp"] + quantity
        if player["hp"] > player["hp_max"] :
            player["hp"] = player["hp_max"]
    if effect == 2 :
        player["hp"] = player["hp"] - quantity
        if player["hp"] < 0 :
            gameOver()

def gameOver() :
    narration(textColor("red","            Y o u   d i e d !                    "), textColor("darkgrey","        Try to do better next time!              "), "")

def displayInventory() :
    clear()
    headerGame()
    printVoid(4)
    print("            [ 1: Weapons ]       [ 2: Boosters ]            ")
    printVoid(1)
    print("            [ 3: Loot    ]       [ 4: Map      ]            ")
    printVoid(1)
    print(textColor("red","                                 [ 5: Close    ]            "))
    printVoid(6)
    footerGame()

def inventoryWeaponsModule(number) :
    if items[0][number]["possessed"] == True :
        if items[0][number]["equiped"] == True :
            print("      [ " + str(number + 1) + ": " + items[0][number]["name"] + " ]  [ " + str(items[0][number]["dmg"]) + "dmg ] " + textColor("blue","[ Equiped ]"))
        else :
            print("      [ " + str(number + 1) + ": " + items[0][number]["name"] + " ]  [ " + str(items[0][number]["dmg"]) + "dmg ] " + textColor("grey","[ Not equiped ]"))
    else :
        print(textColor("darkgrey","      [ " + str(number + 1) + ": " + items[0][number]["name"] + " ]  [ " + str(items[0][number]["dmg"]) + "dmg ] " + textColor("darkgrey","[ Not equiped ]")))
    printVoid(1)

def displayInventoryWeapons() :
    clear()
    headerGame()

    printVoid(1)
    inventoryWeaponsModule(0)
    inventoryWeaponsModule(1)
    inventoryWeaponsModule(2)
    inventoryWeaponsModule(3)
    inventoryWeaponsModule(4)
    inventoryWeaponsModule(5)

    print("      " + textColor("red", "[ 7: Cancel ]"))
    printVoid(1)

    footerGame()

def equipWeapon(number) :

    i = 0

    while i < len(items[0]) :

        if items[0][i]["equiped"] == True :
            items[0][i]["equiped"] = False

        i += 1

    items[0][number]["equiped"] = True

    narration(items[0][number]["name"] + " is now equiped.","","")

def inventoryWeapons(text) :
    displayInventoryWeapons()
    choice = selectOption(text, "displayInventoryWeapons()")

    if choice != 1 and choice != 2 and choice != 3 and choice != 4 and choice != 5 and choice != 6 and choice != 7 :
        inventoryWeapons("> Please enter a valid number.")

    elif choice == 1 and items[0][0]["possessed"] == True :
        displayInventoryWeapons()
        progressiveDisplay("> Loading...")
        time.sleep(0.25)
        equipWeapon(0)
        inventory("> Enter your choice right below.")
    
    elif choice == 2 and items[0][1]["possessed"] == True :
        displayInventoryWeapons()
        progressiveDisplay("> Loading...")
        time.sleep(0.25)
        equipWeapon(1)
        inventory("> Enter your choice right below.")

    elif choice == 3 and items[0][2]["possessed"] == True :
        displayInventoryWeapons()
        progressiveDisplay("> Loading...")
        time.sleep(0.25)
        equipWeapon(2)
        inventory("> Enter your choice right below.")

    elif choice == 4 and items[0][3]["possessed"] == True :
        displayInventoryWeapons()
        progressiveDisplay("> Loading...")
        time.sleep(0.25)
        equipWeapon(3)
        inventory("> Enter your choice right below.")

    elif choice == 5 and items[0][4]["possessed"] == True :
        displayInventoryWeapons()
        progressiveDisplay("> Loading...")
        time.sleep(0.25)
        equipWeapon(4)
        inventory("> Enter your choice right below.")

    elif choice == 6 and items[0][5]["possessed"] == True :
        displayInventoryWeapons()
        progressiveDisplay("> Loading...")
        time.sleep(0.25)
        equipWeapon(5)
        inventory("> Enter your choice right below.")

    elif choice == 7 :
        displayInventoryWeapons()
        progressiveDisplay("> Loading...")
        time.sleep(0.25)
        inventory("> Enter your choice right below.")

    else :
        inventoryWeapons("> Please enter a valid number.")

def inventoryBoostersModule(number) :
    if items[1][number]["possessed"] > 0 :
        print("      [ " + str(number + 1) + ": " + items[1][number]["name"] + " ]  [ +" + str(items[1][number]["effect"]) + "HP ] [ x" + str(items[1][number]["possessed"]) + " ]")
    else :
        print(textColor("darkgrey","      [ " + str(number + 1) + ": " + items[1][number]["name"] + " ]  [ +" + str(items[1][number]["effect"]) + "HP ] [ x" + str(items[1][number]["possessed"]) + " ]"))
    printVoid(1)

def displayInventoryBoosters() :
    clear()
    headerGame()

    printVoid(2)
    inventoryBoostersModule(0)
    inventoryBoostersModule(1)
    inventoryBoostersModule(2)
    inventoryBoostersModule(3)
    inventoryBoostersModule(4)

    print("      " + textColor("red", "[ 6: Cancel ]"))
    printVoid(2)

    footerGame()

def useBooster(number) :

    if items[1][number]["type"] == "battle" :
        hp(1, items[1][number]["effect"])
        items[1][number]["possessed"] = items[1][number]["possessed"] - 1
    elif items[1][number]["type"] == "booster" :
        player["hp_max"] = player["hp_max"] + items[1][number]["effect"]
        hp(1, items[1][number]["effect"])
        items[1][number]["possessed"] = items[1][number]["possessed"] - 1

    narration(items[1][number]["name"] + " has been applied.","","")

def inventoryBoosters(text) :
    displayInventoryBoosters()
    choice = selectOption(text, "displayInventoryBoosters()")

    if choice != 1 and choice != 2 and choice != 3 and choice != 4 and choice != 5 and choice != 6 :
        inventoryBoosters("> Please enter a valid number.")

    elif choice == 1 and items[1][0]["possessed"] > 0 :
        displayInventoryBoosters()
        progressiveDisplay("> Loading...")
        time.sleep(0.25)
        useBooster(0)
        inventory("> Enter your choice right below.")
    
    elif choice == 2 and items[1][1]["possessed"] > 0 :
        displayInventoryBoosters()
        progressiveDisplay("> Loading...")
        time.sleep(0.25)
        useBooster(1)
        inventory("> Enter your choice right below.")

    elif choice == 3 and items[1][2]["possessed"] > 0 :
        displayInventoryBoosters()
        progressiveDisplay("> Loading...")
        time.sleep(0.25)
        useBooster(2)
        inventory("> Enter your choice right below.")
    
    elif choice == 4 and items[1][3]["possessed"] > 0 :
        displayInventoryBoosters()
        progressiveDisplay("> Loading...")
        time.sleep(0.25)
        useBooster(3)
        inventory("> Enter your choice right below.")

    elif choice == 5 and items[1][4]["possessed"] > 0 :
        displayInventoryBoosters()
        progressiveDisplay("> Loading...")
        time.sleep(0.25)
        useBooster(4)
        inventory("> Enter your choice right below.")
    
    elif choice == 6 :
        displayInventoryBoosters()
        progressiveDisplay("> Loading...")
        time.sleep(0.25)
        inventory("> Enter your choice right below.")

    else :
        inventoryBoosters("> Please enter a valid number.")

def inventoryLootModule(number) :
    if items[2][number]["possessed"] > 0 and map_stage_1[player["latitude"]][player["longitude"] - 1]["value"] == 3 :
        print("      [ " + str(number + 1) + ": " + items[2][number]["name"] + " ]  [ +" + str(items[2][number]["value"]) + "@ ] [ x" + str(items[2][number]["possessed"]) + " ]")
    else :
        print(textColor("darkgrey","      [ " + str(number + 1) + ": " + items[2][number]["name"] + " ]  [ +" + str(items[2][number]["value"]) + "@ ] [ x" + str(items[2][number]["possessed"]) + " ]"))
    printVoid(1)

def displayInventoryLoot() :
    clear()
    headerGame()

    printVoid(4)

    inventoryLootModule(0)
    inventoryLootModule(1)
    inventoryLootModule(2)
    
    if map_stage_1[player["latitude"]][player["longitude"] - 1]["value"] == 3 :
        printVoid(1)
    else :
        print(textColor("darkgrey", "      You must be in a camp to be able to sell loot."))
    printVoid(1)

    print("      " + textColor("red", "[ 4: Cancel ]"))
    printVoid(2)

    footerGame()

def sellLoot(number) :

    items[2][number]["possessed"] = items[2][number]["possessed"] - 1

    money(items[2][number]["value"])

def inventoryLoot(text) :
    displayInventoryLoot()
    choice = selectOption(text, "displayInventoryLoot()")

    if choice != 1 and choice != 2 and choice != 3 and choice != 4 :
        inventoryLoot("> Please enter a valid number.")

    elif choice == 1 and items[2][0]["possessed"] > 0 and map_stage_1[player["latitude"]][player["longitude"] - 1]["value"] == 3 :
        displayInventoryLoot()
        progressiveDisplay("> Loading...")
        time.sleep(0.25)
        sellLoot(0)
        inventoryLoot("> Enter your choice right below.")
    
    elif choice == 2 and items[2][1]["possessed"] > 0 and map_stage_1[player["latitude"]][player["longitude"] - 1]["value"] == 3 :
        displayInventoryLoot()
        progressiveDisplay("> Loading...")
        time.sleep(0.25)
        sellLoot(1)
        inventoryLoot("> Enter your choice right below.")

    elif choice == 3 and items[2][2]["possessed"] > 0 and map_stage_1[player["latitude"]][player["longitude"] - 1]["value"] == 3:
        displayInventoryLoot()
        progressiveDisplay("> Loading...")
        time.sleep(0.25)
        sellLoot(2)
        inventoryLoot("> Enter your choice right below.")
    
    elif choice == 4 :
        displayInventoryLoot()
        progressiveDisplay("> Loading...")
        time.sleep(0.25)
        game("> Enter your choice right below.")

    else :
        inventoryLoot("> Please enter a valid number.")

def inventory(text) :

    displayInventory()
    choice = selectOption(text, "displayInventory()")

    if choice != 1 and choice != 2 and choice != 3 and choice != 4 and choice != 5 :
        inventory("> Please enter a valid number.")

    elif choice == 1 :
        displayInventory()
        progressiveDisplay("> Loading...")
        time.sleep(0.25)
        inventoryWeapons("> Enter your choice right below.")

    elif choice == 2 :
        displayInventory()
        progressiveDisplay("> Loading...")
        time.sleep(0.25)
        inventoryBoosters("> Enter your choice right below.")

    elif choice == 3 :
        displayInventory()
        progressiveDisplay("> Loading...")
        time.sleep(0.25)
        inventoryLoot("> Enter your choice right below.")

    elif choice == 4 :
        displayInventory()
        progressiveDisplay("> Loading map data...")
        time.sleep(0.25)
        displayMap(True, "Press Enter to go back.")
        inventory("> Enter your choice right below.")

    elif choice == 5 :
        displayInventory()
        progressiveDisplay("> Closing the menu...")
        time.sleep(0.25)
        game("> Enter your choice right below.")

def displayOptions() :
    clear()
    headerGame()
    printVoid(4)
    if map_stage_1[player["latitude"]][player["longitude"] - 1]["value"] == 3 :
        print("          [ 1: Save     ]       [ 2: Save & quit ]          ")
        printVoid(1)
    else :
        print(textColor("darkgrey","          [ 1: Save     ]       [ 2: Save & quit ]          "))
        print(textColor("darkgrey","          You need to be in a camp to save the game.        "))
    print("          [ 3: Tutorial ]       [ 4: Quit        ]          ")
    printVoid(1)
    print(textColor("red","                                [ 5: Close       ]            "))
    printVoid(6)
    footerGame()

def options(text) :

    displayOptions()
    choice = selectOption(text, "displayOptions()")

    if choice != 1 and choice != 2 and choice != 3 and choice != 4 and choice != 5 :
        options("> Please enter a valid number.")

    elif choice == 1 and map_stage_1[player["latitude"]][player["longitude"] - 1]["value"] == 3 :
        displayOptions()
        progressiveDisplay("> Loading...")
        time.sleep(0.25)
        gameSave(current_save)
        narration("The game was saved!","","")
        game("> Enter your choice right below.")

    elif choice == 2 and map_stage_1[player["latitude"]][player["longitude"] - 1]["value"] == 3 :
        displayOptions()
        progressiveDisplay("> Loading...")
        time.sleep(0.25)
        gameSave(current_save)
        narration("The game was saved! See you soon!")
        launch(True)

    elif choice == 3 :
        displayOptions()
        progressiveDisplay("> Loading...")
        time.sleep(0.25)
        tutorial()
        game("> Enter your choice right below.")

    elif choice == 4 :
        displayOptions()
        progressiveDisplay("> Quitting...")
        time.sleep(0.75)
        printVoid(2)

    elif choice == 5 :
        displayOptions()
        progressiveDisplay("> Closing the menu...")
        time.sleep(0.25)
        game("> Enter your choice right below.")

    else :
        options("> Please enter a valid number.")

def campBuyModule(itemType, number, rank) :
    if itemType == 0 and number == 0 :
        print(textColor("darkgrey","      You have unlocked all the weapons."))
    elif player["money"] < items[itemType][number]["price"] :
        print(textColor("darkgrey","      [ " + str(rank) + ": " + items[itemType][number]["name"] + " ]  ( " + textColor("red",str(items[itemType][number]["price"])+"@") + " )"))
    else :
        print("      [ " + str(rank) + ": " + items[itemType][number]["name"] + " ]  ( " + textColor("red",str(items[itemType][number]["price"])+"@") + " )")
    printVoid(1)

def displayCampBuy(temp) :
    clear()
    headerGame()

    printVoid(4)

    campBuyModule(0, temp, 1)
    campBuyModule(1, 1, 2)
    campBuyModule(1, 3, 3)
    
    printVoid(2)

    print("      " + textColor("red", "[ 4: Cancel ]"))
    printVoid(2)

    footerGame()

def buyItem(number1, number2) :

    if number1 == 0 :
        items[number1][number2]["possessed"] = True
        player["money"] = player["money"] - items[number1][number2]["price"]
    if number1 == 1 : 
        items[number1][number2]["possessed"] = items[number1][number2]["possessed"] + 1
        player["money"] = player["money"] - items[number1][number2]["price"]

    narration(items[number1][number2]["name"] + " was successfully purchased.","","")

def campBuyWeapon() :
    i = 0
    while i < len(items[0]) :
        if items[0][i]["possessed"] == False :
            return i
        i = i + 1
    return 0

def campBuy(text) :
    weaponBuyable = campBuyWeapon()
    displayCampBuy(weaponBuyable)
    choice = selectOption(text, "displayCampBuy(" + str(weaponBuyable) + ")")

    if choice != 1 and choice != 2 and choice != 3 and choice != 4 :
        campBuy("> Please enter a valid number.")

    elif choice == 1 and player["money"] >= items[0][weaponBuyable]["price"]:
        displayCampBuy(weaponBuyable)
        progressiveDisplay("> Loading...")
        time.sleep(0.25)
        buyItem(0, weaponBuyable)
        campBuy("> Enter your choice right below.")
    
    elif choice == 2 and player["money"] >= items[1][1]["price"]:
        displayCampBuy(weaponBuyable)
        progressiveDisplay("> Loading...")
        time.sleep(0.25)
        buyItem(1, 1)
        campBuy("> Enter your choice right below.")

    elif choice == 3 and player["money"] >= items[1][3]["price"]:
        displayCampBuy(weaponBuyable)
        progressiveDisplay("> Loading...")
        time.sleep(0.25)
        buyItem(1, 3)
        campBuy("> Enter your choice right below.")
    
    elif choice == 4 :
        displayCampBuy(weaponBuyable)
        progressiveDisplay("> Loading...")
        time.sleep(0.25)
        game("> Enter your choice right below.")

    else :
        campBuy("> Please enter a valid number.")

def displayCampInteractions() :
    clear()
    headerGame()

    printVoid(4)
    print("                 -*- Camp Interactions -*-                  ")
    printVoid(1)

    if player["money"] > 3 and player["hp"] != player["hp_max"] :
        print("                  [ 1: Heal " + textColor("red","(Costs 4 @)") + " ]                  ")
    else :
        print(textColor("darkgrey","                  [ 1: Heal (Costs 4 @) ]                  "))
    printVoid(1)
    print("                  [ 2: Buy items         ]                  ")
    printVoid(1)
    print("                  [ 3: Sell loot         ]                  ")
    printVoid(1)

    print("                             " + textColor("red", "[ 4: Cancel ]"))
    printVoid(2)

    footerGame()

def campHeal() :
    player["money"] = player["money"] - 4
    player["hp"] = player["hp_max"]
    narration("Your health was fully restored","",textColor("red","[ -4 @ ]"))

def campInteractions(text) :
    displayCampInteractions()
    choice = selectOption(text, "displayCampInteractions()")

    if choice != 1 and choice != 2 and choice != 3 and choice != 4 :
        campInteractions("> Please enter a valid number.")

    elif choice == 1 and player["money"] > 9 and player["hp"] != player["hp_max"] :
        displayCampInteractions()
        progressiveDisplay("> Loading...")
        time.sleep(0.25)
        campHeal()
        campInteractions("> Enter your choice right below.")
    
    elif choice == 2 :
        displayCampInteractions()
        progressiveDisplay("> Loading...")
        time.sleep(0.25)
        campBuy("> Enter your choice right below.")

    elif choice == 3 :
        displayCampInteractions()
        progressiveDisplay("> Loading...")
        time.sleep(0.25)
        inventoryLoot("> Enter your choice right below.")
    
    elif choice == 4 :
        displayCampInteractions()
        progressiveDisplay("> Loading...")
        time.sleep(0.25)
        game("> Enter your choice right below.")

    else :
        campInteractions("> Please enter a valid number.")

def displayPlayerRound(ename, ehp, mob, msg) :
    clear()
    headerGame()

    hp_bars = (float(player["hp"]) / float(player["hp_max"])) * 12
    hp_bars = int(hp_bars)
    hp_to_display = ""

    i = 0
    while i < 12 :
        if i < hp_bars :
            hp_to_display = hp_to_display + textColor("green","|")
        else :
            hp_to_display = hp_to_display + textColor("darkgrey","|")
        i = i + 1

    enemy_hp_bars = (float(ehp) / float(mobs[mob]["hp"])) * 12
    enemy_hp_bars = int(enemy_hp_bars)
    enemy_hp_to_display = ""

    i = 0
    while i < 12 :
        if i < enemy_hp_bars :
            enemy_hp_to_display = enemy_hp_to_display + textColor("green","|")
        else :
            enemy_hp_to_display = enemy_hp_to_display + textColor("darkgrey","|")
        i = i + 1

    printVoid(1)
    print(textColor("red","                       -*- Battle -*-                       "))
    printVoid(1)
    print("     " + ename)
    print(">   [" + enemy_hp_to_display + "]                                          ")
    printVoid(2)
    print(">   " + msg)
    printVoid(2)
    print("                                                    You     ")
    print("                                          [" + hp_to_display + "]   <")
    printVoid(1)
    print("    [ 1: Attack ]     [ 2 : Inventory ]      [ 3 : Run ]    ")
    printVoid(1)

    footerGame()

def playerRound(text, ename, ehp, mob) :
    
    displayPlayerRound(ename, ehp, mob, "")
    choice = selectOption(text, 'displayPlayerRound("' + str(ename) + '",' + str(ehp) + "," + str(mob) + "," + '" "' + ")" )

    if choice != 1 and choice != 2 and choice != 3 :
        playerRound("> Please enter a valid number.", ename, ehp, mob)

    elif choice == 1 :
        playerdmg = 0
        i = 0
        while i < len(items[0]) :

            if items[0][i]["equiped"] == True :
                playerdmg = items[0][i]["dmg"]
            i += 1

        dmgmultiplicator = float(player["level"]) / 10
        playerdmg = float(playerdmg) * (1 + dmgmultiplicator)
        playerdmg = int(playerdmg)

        if random.randint(0,100) < 15 :
            ehp1 = ehp - (playerdmg * 2)
            return ehp1, False, textColor("blue", "CRITICAL HIT! ")  + "You dealt " + textColor("blue",str(playerdmg * 2) + " damage") + " to the " + ename + "!"
        else :
            ehp1 = ehp - playerdmg
            return ehp1, False, "You dealt " + str(playerdmg) + " damage to the " + ename + "!"
    
    elif choice == 2 :
        inventoryBattle("> Enter your choice right below.")

        return ehp, False, ""

    elif choice == 3 :
        abandon = False
        if random.randint(0,100) < 33 :
            abandon = True
            narration("You successfully ran away!","","")
        else :
            narration("You did not manage to run away...","You must continue the battle.","")
        return ehp, abandon, ""


def debutBattle(mob) :
    enemy_name = mobs[mob]["name"]
    enemy_hp = mobs[mob]["hp"]
    enemy_dmg = mobs[mob]["dmg"]
    abandon = False

    while enemy_hp > 0 and player["hp"] > 0 and abandon == False :
        enemy_hp, abandon, msg = playerRound("> Enter your choice right below.", enemy_name, enemy_hp, mob)

        if abandon == False :
            displayPlayerRound(enemy_name, enemy_hp, mob, msg)
            pressEnter("> Press Enter to continue...")

            if enemy_hp > 0 :
                dmgmultiplicator = float(player["level"] + 1) / 10
                enemy_dmg2 = float(enemy_dmg) * (1 + dmgmultiplicator)
                enemy_dmg2 = int(enemy_dmg2)

                if random.randint(0,100) < 15 :
                    player["hp"] = player["hp"] - (enemy_dmg2 * 2)
                    displayPlayerRound(enemy_name, enemy_hp, mob, textColor("blue", "CRITICAL HIT! ") + "The " + enemy_name + " hit you and dealt you " + textColor("blue", str(enemy_dmg2 * 2) + " damage!"))
                else :
                    player["hp"] = player["hp"] - enemy_dmg2
                    displayPlayerRound(enemy_name, enemy_hp, mob, "The " + enemy_name + " hit you and dealt you " + str(enemy_dmg2) + " damage!")
                pressEnter("> Press Enter to continue...")

    if player["hp"] < 1 :
        gameOver()
        sys.exit()
    elif enemy_hp < 1 and mob != 3 :
        bonusmultiplicator = float(player["level"]) / 4
        xp_reward = random.randint(40,70) * (1 + bonusmultiplicator)
        xp_reward = int(xp_reward)

        money_reward = random.randint(2,8) * (1 + bonusmultiplicator)
        money_reward = int(money_reward)

        if random.randint(0,100) < 1 :
            items[2][2]["possessed"] = items[2][2]["possessed"] + 1
            narrationGame("Congratulations! You managed to kill the " + enemy_name + "!","The " + enemy_name + " you killed dropped a " + textColor("red",items[2][2]["name"]) + "!", "The new item has been transfered to your inventory.")
        elif random.randint(0,100) < 4 :
            items[2][1]["possessed"] = items[2][1]["possessed"] + 1
            narrationGame("Congratulations! You managed to kill the " + enemy_name + "!","The " + enemy_name + " you killed dropped a " + textColor("blue",items[2][1]["name"]) + "!", "The new item has been transfered to your inventory.")
        elif random.randint(0,100) < 8 :
            items[2][0]["possessed"] = items[2][0]["possessed"] + 1
            narrationGame("Congratulations! You managed to kill the " + enemy_name + "!","The " + enemy_name + " you killed dropped a " + textColor("green",items[2][0]["name"]) + "!", "The new item has been transfered to your inventory.")
        else :
            narrationGame("Congratulations! You managed to kill the " + enemy_name + "!","","")

        xp(xp_reward)
        money(money_reward)
    elif enemy_hp < 1 and mob == 3 :
        bonusmultiplicator = float(player["level"]) / 4
        xp_reward = random.randint(1000,3500) * (1 + bonusmultiplicator)
        xp_reward = int(xp_reward)

        money_reward = random.randint(2,8) * (1 + bonusmultiplicator)
        money_reward = int(money_reward)

        xp(xp_reward)
        money(money_reward)

        narrationGame("You got rid of the giant Mammoth, well done!","However, what you thought was the end of a crazy story,","only seems to be the beginning of it...")

        



# Battle inventory

def inventoryWeaponsBattle(text) :
    displayInventoryWeapons()
    choice = selectOption(text, "displayInventoryWeapons()")

    if choice != 1 and choice != 2 and choice != 3 and choice != 4 and choice != 5 and choice != 6 and choice != 7 :
        inventoryWeaponsBattle("> Please enter a valid number.")

    elif choice == 1 and items[0][0]["possessed"] == True :
        displayInventoryWeapons()
        progressiveDisplay("> Loading...")
        time.sleep(0.25)
        equipWeapon(0)
    
    elif choice == 2 and items[0][1]["possessed"] == True :
        displayInventoryWeapons()
        progressiveDisplay("> Loading...")
        time.sleep(0.25)
        equipWeapon(1)

    elif choice == 3 and items[0][2]["possessed"] == True :
        displayInventoryWeapons()
        progressiveDisplay("> Loading...")
        time.sleep(0.25)
        equipWeapon(2)

    elif choice == 4 and items[0][3]["possessed"] == True :
        displayInventoryWeapons()
        progressiveDisplay("> Loading...")
        time.sleep(0.25)
        equipWeapon(3)

    elif choice == 5 and items[0][4]["possessed"] == True :
        displayInventoryWeapons()
        progressiveDisplay("> Loading...")
        time.sleep(0.25)
        equipWeapon(4)

    elif choice == 6 and items[0][5]["possessed"] == True :
        displayInventoryWeapons()
        progressiveDisplay("> Loading...")
        time.sleep(0.25)
        equipWeapon(5)

    elif choice == 7 :
        displayInventoryWeapons()
        progressiveDisplay("> Loading...")
        time.sleep(0.25)
        inventoryBattle("> Enter your choice right below.")

    else :
        inventoryWeaponsBattle("> Please enter a valid number.")

def inventoryBoostersBattle(text) :
    displayInventoryBoosters()
    choice = selectOption(text, "displayInventoryBoosters()")

    if choice != 1 and choice != 2 and choice != 3 and choice != 4 and choice != 5 and choice != 6 :
        inventoryBoostersBattle("> Please enter a valid number.")

    elif choice == 1 and items[1][0]["possessed"] > 0 :
        displayInventoryBoosters()
        progressiveDisplay("> Loading...")
        time.sleep(0.25)
        useBooster(0)
    
    elif choice == 2 and items[1][1]["possessed"] > 0 :
        displayInventoryBoosters()
        progressiveDisplay("> Loading...")
        time.sleep(0.25)
        useBooster(1)

    elif choice == 3 and items[1][2]["possessed"] > 0 :
        displayInventoryBoosters()
        progressiveDisplay("> Loading...")
        time.sleep(0.25)
        useBooster(2)
    
    elif choice == 4 and items[1][3]["possessed"] > 0 :
        displayInventoryBoosters()
        progressiveDisplay("> Loading...")
        time.sleep(0.25)
        useBooster(3)

    elif choice == 5 and items[1][4]["possessed"] > 0 :
        displayInventoryBoosters()
        progressiveDisplay("> Loading...")
        time.sleep(0.25)
        useBooster(4)
    
    elif choice == 6 :
        displayInventoryBoostersBattle()
        progressiveDisplay("> Loading...")
        time.sleep(0.25)
        inventoryBattle("> Enter your choice right below.")

    else :
        inventoryBoosters("> Please enter a valid number.")

def displayInventoryBattle() :
    clear()
    headerGame()
    printVoid(4)
    print("            [ 1: Weapons ]       [ 2: Boosters ]            ")
    printVoid(1)
    print("            " + textColor("darkgrey","[ 3: Loot    ]" )+ "       [ 4: Map      ]            ")
    printVoid(1)
    print(textColor("red","                                                            "))
    printVoid(6)
    footerGame()

def inventoryBattle(text) :

    displayInventoryBattle()
    choice = selectOption(text, "displayInventoryBattle()")

    if choice != 1 and choice != 2 and choice != 3 and choice != 4 :
        inventoryBattle("> Please enter a valid number.")

    elif choice == 1 :
        displayInventoryBattle()
        progressiveDisplay("> Loading...")
        time.sleep(0.25)
        inventoryWeaponsBattle("> Enter your choice right below.")

    elif choice == 2 :
        displayInventoryBattle()
        progressiveDisplay("> Loading...")
        time.sleep(0.25)
        inventoryBoostersBattle("> Enter your choice right below.")

    elif choice == 3 :
        inventoryBattle("> Loots are not available during battle.")

    elif choice == 4 :
        displayInventoryBattle()
        progressiveDisplay("> Loading map data...")
        time.sleep(0.25)
        displayMap(True, "Press Enter to go back.")
        inventoryBattle("> Enter your choice right below.")

# Launching the game

launch(True)