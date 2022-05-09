from clear import clear
from rich import print as rprint
from time import sleep
import random
from saveloader import editSystemSave,editSettingsFile, addSystemSave
from checkbadge import calculateBadge

# shutdown woohoo
def shutdown():
    clear()
    print('V E U I L L E Z  P A C I E N T E R . . .\n\n\n')
    sleep(3)
    rprint('[bold yellow]Vous pouvez fermer le jeu en toute sécurité.[/bold yellow]')
    sleep(2)
    quit()

def restart():
    clear()
    print('V E U I L L E Z  P A C I E N T E R . . .\n\n\n')
    sleep(3)
    from boot import boot
    boot()

def settings(systemname, systemlevel, systempro, settingsdict):
    clear()
    print('╔════════════════════════╗\n║     O P T I O N S      ║\n║    1 - Popup           ║\n║    2 - Retour          ║\n╚════════════════════════╝\n')
    choise = input("> ")
    if choise == "1":
        clear()
        print("Voulez-vous prendre cette barre :")
        rprint("\nVotre barre:[blue][][][][][][][][][][][][][][][][][][][][/blue]")
        print('Vous avez 95% dans votre progressbar')
        print("\nAller vers le popup? (Y/N)")
        print(settingsdict)
        choice = input("> ")
        if choice == "Y" or choice =="y":
            editSettingsFile("screenDown", "True", settingsdict)
            settings(systemname, systemlevel, systempro, settingsdict)
        elif choice == "N" or choice == "n":   
            editSettingsFile("screenDown", "False", settingsdict)
            settings(systemname, systemlevel, systempro, settingsdict)
        else:
            settings(systemname, systemlevel, systempro, settingsdict)
    elif choise == "2":
        beginMenu(systemname, systemlevel, systempro, settingsdict)
    else:
        settings(systemname, systemlevel, systempro, settingsdict)

# Begin menu normally
def beginMenu(systemname, systemlevel, systempro, settingsdict):
    clear()
    if systemname == "95":
        if systemlevel > 1:
            print('╔════════════════════════╗\n║     M e n u   ║\n║    1 - Charger le jeu       ║\n║    2 - Nouveau jeu        ║\n║    3 - Redémarrer         ║\n║    4 - éteindre        ║\n╚════════════════════════╝\n')
        else:
            print('╔════════════════════════╗\n║    M e n u   ║\n║    1 - Nouveau jeu        ║\n║    2 - Redémarrer         ║\n║    3 - éteindre        ║\n╚════════════════════════╝\n')
    else:
        if systemlevel > 1:
            print('╔════════════════════════╗\n║    M e n u   ║\n║    1 - Charger le jeu       ║\n║    2 - Nouveau jeu        ║\n║    3 - Paramètres        ║\n║    4 - Redémarrer         ║\n║    5 - éteindre        ║\n╚════════════════════════╝\n')
        else:
            print('╔════════════════════════╗\n║    M e n u   ║\n║    1 - Nouveau jeu        ║\n║    2 - Paramètres        ║\n║    3 - Redémarrer         ║\n║    4 - éteindre        ║\n╚════════════════════════╝\n')
    choice = input("> ")
    if choice == "1":
        if systemlevel > 1:
            startGame(systemname, systemlevel, systempro, settingsdict)
        else:
            editSystemSave(systemname, 1)
            startGame(systemname, 1, systempro, settingsdict)
    elif choice == "2":
        if systemname == "95":
            if systemlevel > 1:
                editSystemSave(systemname, 1)
                startGame(systemname, 1, systempro, settingsdict)
            else:
                restart()
        else: 
            if systemlevel > 1:
                editSystemSave(systemname, 1)
                startGame(systemname, 1, systempro, settingsdict)
            else:
                settings(systemname, systemlevel, systempro, settingsdict)
    elif choice == "3":
        if systemname == "95":
            if systemlevel > 1:
                restart()
            else:
                shutdown()
        else:
            if systemlevel > 1:
                settings(systemname, systemlevel, systempro, settingsdict)
            else:
                restart()
    elif choice == "4":
        if systemname == "95":
            if systemlevel > 1:
                shutdown()
            else:
                beginMenu(systemname, systemlevel, systempro, settingsdict)
        else:
            if systemlevel > 1:
                restart()
            else: 
                shutdown()
    elif choice == "5":
        if systemname == "95":
            beginMenu(systemname, systemlevel, systempro, settingsdict)
        else:
            if systemlevel > 1:
                shutdown()
    else:
        beginMenu(systemname, systemlevel, systempro, settingsdict)


# Begin menu during gameplay
def pauseBeginMenu(systemName, systemPro):
    clear()
    print('╔════════════════════════╗\n║    M e n u   ║\n║    1 - Reprendre          ║\n║    2 - Nouveau jeu        ║\n║    3 - Redémarrer         ║\n║    4 - éteindre        ║\n╚════════════════════════╝\n')
    choice = input()
    if choice == "1":
        return
    elif choice == "2":
        editSystemSave(systemName, 1)
        startGame(systemName, 1, systemPro)
    elif choice == "3":
        restart()
    elif choice == "4":
        shutdown()
    else:
        pauseBeginMenu(systemName, systemPro)

# original code by Setapdede, but i refined it a bit.
def spawnPopup(startLevel, systemLabel, settingsdict):
    clear()
    print('Level', startLevel)
    if systemLevel > 0:
        print('<', systemLabel, '>')
    rprint("[bold bright_black]╔════════════════════╗\n║[/bold bright_black] :) Ceci est une pub ennuyeuse! [bold bright_black]║\n║[/bold bright_black]        [OK]        [bold bright_black]║\n╚════════════════════╝[/bold bright_black]")
    if settingsdict.get("screenDown") == "True":
        screenDownFun()
    popupinput = input()
    if popupinput == "OK":
        clear()
    elif popupinput == "ok":
	    clear()
    else:
        spawnPopup(startLevel, systemLabel, settingsdict)

def screenDownFun():
    # checks if you have orange segments in your bar
    if progressbar2 > 0:
        print('\nYour bar:', end='')
        for segment in bar2:
            if segment == "Blue":
                rprint("[blue][][/blue]", end='')
            elif segment == "Orange":
                rprint("[bright_yellow][][/bright_yellow]", end='')
        print("\nVous avez", progressbar, "% avec", progressbar2, "% d'orange dans votre progressbar.")
    else:
        print('\nYour bar:', end='')
        for segment in bar2:
            if segment == "Blue":
                rprint("[blue][][/blue]", end='')
        print("\nVous avez", progressbar,"%", "dans votre progressbar.")

def startGame(systemName, startLevel, proLevel, settingsdict):
    global progressbar # total progressbar progress
    global progressbar2 # total orange segments in progressbar
    global lives
    global score
    global bar # array that contains segments for the progressbar
    global bar2 # contents in bar that are used to calculate pink segments
    global bardisplay # bar[] contents are displayed on screen
    global segments # used in conjunction with bardisplay
    global systemLabel # current system label
    global systemLevel # current system level (used with systemLabel)

    # setting global variables
    progressbar = 0
    progressbar2 = 0
    lives = 3
    score = 0
    bar = []
    bar2 = []
    bardisplay = ""
    segments = ""

    systemLabel = calculateBadge(startLevel, proLevel)

    if systemLabel == "What?":
        systemLevel = 6
    elif systemLabel == "Grand":
        systemLevel = 5
    elif systemLabel == "Adept":
        systemLevel = 4
    elif systemLabel == "Master":
        systemLevel = 3
    elif systemLabel == "Expert":
        systemLevel = 2
    elif systemLabel == "Pro":
        systemLevel = 1
    else:
        systemLevel = 0

    while True:
        # clears the screen for next segment
        clear()

        # checks if lives are 0, breaks if true
        if lives == 0:
            rprint("[bold bright_blue]Vous avez plus de vie. Game over![/bold bright_blue]")
            if startLevel == 1:
                rprint('[i]A level has not been taken.[/i]')
            else:
                startLevel -= 1
                rprint('[bold i]-1 Level[/bold i]')
                editSystemSave(systemName, startLevel)
            lives = 3
            sleep(3)
            clear()

        popupshow = random.randint(0, 6)
        if popupshow == 6:
            spawnPopup(startLevel, systemLabel, settingsdict)

        print('Level', startLevel)
        if systemLevel > 0:
            print('<', systemLabel, '>')

        # randomly chooses a segment and loads art
        seg = random.randint(0, 5)
        if seg == 0:
            rprint("[blue]╔══╗\n║  ║\n║  ║\n╚══╝[/blue]")
        elif seg == 1:
            rprint("[bright_red]╔══╗\n║!!║\n║!!║\n╚══╝[/bright_red]")
        elif seg == 2:
            rprint("[bright_magenta]╔══╗\n║--║\n║--║\n╚══╝[/bright_magenta]")
        elif seg == 3:
            rprint("[yellow]╔══╗\n║~~║\n║~~║\n╚══╝[/yellow]")
        elif seg == 4:
            rprint("[bright_black]╔══╗\n║..║\n║..║\n╚══╝[/bright_black]")
        elif seg == 5:
            rprint("[bright_cyan]╔══╗\n║**║\n║**║\n╚══╝[/bright_cyan]")

        # green segment check
        greenseg = random.randint(0, 100)
        if greenseg == 95:
            clear()
            print('Level', startLevel)
            if systemLevel > 0:
                print('<', systemLabel, '>')
            seg = 6
            rprint("[bright_green]╔══╗\n║$$║\n║$$║\n╚══╝[/bright_green]")

        # checks if you have 1 life left
        if lives == 1:
            rprint("Vous n'avez [italic bright_red]Plus qu'une vie [/italic bright_red]. Attention, au prochain échec, c'est le game over .")
        else:
            print("Vous avez", lives, "vies.")
        
        screenDownFun()

        # catches the currently displayed segment
        catch = input("Appyuez 'c' pour attraper, Appuyez sur n'importe quelle touche pour esquiver, et 'q' pour quitter.\n> ")

        # calculates which segment you caught and does stuff
        if seg == 0 and catch == "c":
            progressbar = progressbar + 5
            bar2.append("Blue")
            score = score + 5
        elif seg == 1 and catch == "c":
            bar = []
            bar2 = []
            bardisplay = ""
            lives = lives - 1
            progressbar = 0
            progressbar2 = 0
            score = score - 10
        elif seg == 2 and catch == "c":
            if progressbar == 0:
                continue
            if bar2[-1] == "Orange":
                progressbar2 = progressbar2 - 5
                progressbar = progressbar - 5
                bar2.pop(-1)
                score = score + 5
            else:
                progressbar = progressbar - 5
                bar2.pop(-1)
                score + score - 5
        elif seg == 3 and catch == "c":
            progressbar = progressbar + 5
            progressbar2 = progressbar2 + 5
            bar2.append("Orange")
        elif seg == 4 and catch == "c":
            continue
        elif seg == 5 and catch == "c":
            bonus = random.randint(0, 1)
            if bonus == 0:
                progressbar = progressbar + 10
                bar2.append("Blue")
                bar2.append("Blue")
                score = score + 10
            else:
                progressbar = progressbar + 15
                bar2.append("Blue")
                bar2.append("Blue")
                bar2.append("Blue")
                score = score + 15
        elif seg == 6 and catch == "c":
            progressbar = 100
            progressbar2 = 0
            score = score + 100

        if catch == "q":
            print('Processus interrompu! Merci d\'avoir joué!')
            sleep(3)
            beginMenu(systemName, startLevel, proLevel, settingsdict)

        if catch == "beginmenu":
            pauseBeginMenu(systemName, proLevel)

        # if you have 100% on your progressbar, the game will end.
        if progressbar >= 100:
            if progressbar2 > 0:
                print('Bravo!')
            elif progressbar >= 100 and progressbar2 == 0:
                print('Parfait!')
            elif progressbar > 100:
                print('Espace saturé!')
            if progressbar == 50 and progressbar2 == 50:
                print ('Yin et yang')
            if progressbar == 0 and progressbar2 == 100:
                print ("Non-conformiste!")
            startLevel += 1
            editSystemSave(systemName, startLevel)
            if startLevel == proLevel:
                print('\nBravo! Vous êtes devenu un Professionel!')
                print('Pro Label acquis!')
                systemLevel = 1
                systemLabel = "Pro"
            elif startLevel == 15 and systemName == "95":
                print('Progressbar95 plus débloqué...')
                addSystemSave("95plus")
            elif startLevel == 25 and systemName == "95plus":
                print ('Progressbar98 débloqué...')
                addSystemSave("98")
            elif startLevel == 30 and systemName == "98":
                print ('ProgressbarMeme débloqué...')
                addSystemSave("Meme")
            elif startLevel == 100:
                print('\nExpert Label acquis!')
                systemLevel = 2
                systemLabel = "Expert"
            elif startLevel == 250:
                print('\nMaster Label acquis!')
                systemLevel = 3
                systemLabel = "Master"
            elif startLevel == 500:
                print('\nAdept Label acquis!')
                systemLevel = 4
                systemLabel = "Adept"
            elif startLevel == 1000:
                print('\nGrand Label acquis!')
            elif startLevel == 2147483647:
                print('\nWhat the hell?! how?!')
                systemLevel = 5
                systemLabel = "Grand"
            bar = []
            bar2 = []
            bardisplay = ""
            segments = ""
            progressbar = 0
            progressbar2 = 0
            print('\nPressez ENTER pour passer au niveau supérieur.')
            input()
        continue
