import sys
sys.path.insert(0, '../')
from clear import clear
from time import sleep
from player import startGame, beginMenu, pauseBeginMenu

def launchwolfos(systemlevel, systembadge, systempro, settingsdict):
    clear()
    print('P r o g r e s s W o l f  O S')
    print(systembadge)
    print('\n\n\nChargement...')
    sleep(5)
    beginMenu("wolfos", systemlevel, systempro, settingsdict)
