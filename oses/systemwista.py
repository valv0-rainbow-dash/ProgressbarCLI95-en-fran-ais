import sys
sys.path.insert(0, '../')
from clear import clear
from time import sleep
from player import startGame, beginMenu, pauseBeginMenu

# How about some uniqueness to these things? I can just do these by copypasting them.
# Just a suggestion.
def launchwista(systemlevel, systembadge, systempro, settingsdict):
    clear()
    print('P r o g r e s s b a r  W i s t a')
    print(systembadge)
    print('\n\n\nChargement...')
    sleep(6)
    beginMenu("wista", systemlevel, systempro, settingsdict)