from saveloader import detectSave,detectSettings, loadSystemSave, loadSettingsSave
from rich import print as rprint
from clear import clear
from checkbadge import calculateBadge
import sys

# system pros
global pro95
global pro95plus
global pro98
global promeme
global pro2000
global proxb
global prowista

pro95 = 10
pro95plus = 20
pro98 = 20
promeme = 30
pro2000 = 30
proxb = 40
prowista = 40

# systems
sys.path.insert(0, './oses/')


def startup(system):
    from system95 import launch95
    from system95plus import launch95plus
    from system98 import launch98
    from systemmeme import launchmeme
    from system2000 import launch2000
    from systemxb import launchxb
    from systemwista import launchwista
    if system == "1":
        level95 = loadSystemSave("95")
        badge95 = calculateBadge(level95, pro95)
        launch95(level95, badge95, pro95, settingsdict)
    elif system == "2":
        plus95check = loadSystemSave("95plus")
        badge95plus = calculateBadge(plus95check, pro95plus)
        if plus95check == False:
            boot()
        else:
            launch95plus(plus95check, badge95plus, pro95plus, settingsdict)
    elif system == "3":
        check98 = loadSystemSave("98")
        badge98 =  calculateBadge (check98, pro98)
        if check98 == False:
            boot()
        else:
            launch98(check98, badge98, pro98, settingsdict)
    elif system == "4":
        checkmeme = loadSystemSave("Meme")
        badgememe =  calculateBadge (checkmeme, promeme)
        if checkmeme == False:
            boot()
        else:
            launchmeme(checkmeme, badgememe, promeme, settingsdict)
    elif system == "5":
        check2000 = loadSystemSave("2000")
        badge2000 =  calculateBadge (check2000, pro2000, settingsdict)
        if check2000 == False:
            boot()
        else:
            launch2000(check2000, badge2000, pro2000, settingsdict)
    elif system == "6":
        checkxb = loadSystemSave("xb")
        badgexb =  calculateBadge(checkxb, proxb)
        if checkxb == False:
            boot()
        else:
            launchxb(checkxb, badgexb, proxb, settingsdict)
    elif system == "7":
       checkwista = loadSystemSave("wista")
       # bruh !!!! -716
       badgewista = calculateBadge(checkwista, prowista)
       if checkwista == False:
          boot()
       else:
           launchwista(checkwista, badgewista, prowista, settingsdict)
def boot():

    detectSave()
    detectSettings()

    global settingsdict
    settingsdict = loadSettingsSave()

    global currentSystem

    clear()
    
    # btw pivin fucking work on sparrow
    # it's just a decision tree, isn't too hard.
    # or at least sounds easy.
    rprint('[white]Sparrow Assistant Enhanced Text BIOS.[not bold]80.1[/not bold][/white] - [bright_yellow]Energy Star (un)Powered[/bright_yellow]')
    rprint('[white]CLI ver. [bold]0.2.2a-fr-fix[/bold] - compiled 05-09-2022[/white]\n\n')

    ninefive = loadSystemSave("95")
    ninefivebadge = calculateBadge(ninefive, pro95)
    print('1. Progressbar 95', ninefivebadge)

    ninefiveplus = loadSystemSave("95plus")
    if ninefiveplus == False:
        rprint('[red][not bold]2[/not bold]. Progressbar [not bold]95[/not bold] Plus - Passez le niveau 15 dans PB95 pour débloquer cela![/red]')
    else:
        ninefiveplusbadge = calculateBadge(ninefiveplus, pro95plus)
        print('2. Progressbar 95 Plus', ninefiveplusbadge)

    nineeight = loadSystemSave("98")
    if nineeight == False:
        rprint('[red][not bold]3[/not bold]. Progressbar [not bold]98[/not bold] - Passez le niveau 25 dans PB95+ pour débloquer cela![/red]')
    else:
        nineeightbadge = calculateBadge(nineeight, pro98)
        print ('3. Progressbar 98', nineeightbadge)
    meme = loadSystemSave("Meme")
    if meme == False:
        rprint('[red][not bold]4[/not bold]. Progressbar Meme - Passez le niveau 30 dans PB98 pour débloquer cela![/red]')
    else:
        memebadge = calculateBadge(meme, promeme)
        print ('4. Progressbar Meme', memebadge)
    twok = loadSystemSave("2000")
    if twok == False:
        rprint('[red][not bold]5[/not bold]. Progressbar [not bold]2000[/not bold] - Passez le niveau 30 dans PBMeme pour débloquer cela![/red]')
    else:
        twokbadge = calculateBadge(twok, pro2000)
        print ('5. Progressbar 2000', twokbadge)
    xb = loadSystemSave("xb")
    if xb == False:
        rprint('[red][not bold]6[/not bold]. Progressbar XB - Passez le niveau 40 dans PB2000 pour débloquer cela![/red]')
    else:
        xbbadge = calculateBadge(xb, proxb)
        print ('6. Progressbar XB', xbbadge)
    wista = loadSystemSave("Wista")
    if wista == False:
        rprint('[red][not bold]7[/not bold]. Progressbar Wista - Passez le niveau 50 dans PBXB pour débloquer cela![/red]')
    else:
         wistabadge = calculateBadge(wista, prowista)
         print('7. Progressbar Wista (INCOMPLETE)', wistabadge)


    choice = input()
    startup(choice)

boot()
