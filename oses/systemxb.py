import sys
sys.path.insert(0, '../')
from clear import clear
from time import sleep
from player import startGame, beginMenu, pauseBeginMenu

def launchxb(systemlevel, systembadge, systempro, settingsdict):
    clear()
    print('P r o g r e s s b a r  X B')
    print(systembadge)
    print('\n\n\nChargement...')
    sleep(5)
    beginMenu("xb", systemlevel, systempro, settingsdict)
