import sys
sys.path.insert(0, '../')
from clear import clear
from time import sleep
from player import startGame, beginMenu, pauseBeginMenu

def launch95(systemlevel, systembadge, systempro, settingsdict):
    clear()
    print('P r o g r e s s b a r  9 5')
    print(systembadge)
    print('\n\n\nChargement...')
    sleep(4)
    beginMenu("95", systemlevel, systempro, settingsdict)
