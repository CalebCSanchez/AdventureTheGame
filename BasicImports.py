#Basic imports
from random import *
from sys import stdout
from time import sleep
from winsound import PlaySound, SND_ASYNC, SND_LOOP
from sys import exit
def print_medium(str):
    for letter in str:
        stdout.write(letter)
        stdout.flush()
        sleep(0.045)
def print_reallyslow(str):
    for letter in str:
        stdout.write(letter)
        stdout.flush()
        sleep(0.25)
def print_slow(str):
    for letter in str:
        stdout.write(letter)
        stdout.flush()
        sleep(0.1)
def print_fast(str):
    for letter in str:
        stdout.write(letter)
        stdout.flush()
        sleep(0.03)
intromusic="C:/Users/caleb_000/Documents/Python/Python Game/Music/8-Bit Mix- Music Box - Dark Cloud.wav"
normaldaymusic="C:/Users/caleb_000/Documents/Python/Python Game/Music/Dark Cloud Main Theme 8 Bit Remix (1).wav"
beginningbattlemusic="C:/Users/caleb_000/Documents/Python/Python Game/Music/Kingdom Hearts 2 -  The Encounter  8-bit.wav"
wizardmusic="C:/Users/caleb_000/Documents/Python/Python Game/Music/8 Bit Mix - One Winged Angel.wav"
crashingdownmusic="C:/Users/caleb_000/Documents/Python/Python Game/Music/Sonic Advance 2 Soundtrack- Final Ending.wav"
endgamemusic="C:/Users/caleb_000/Documents/Python/Python Game/Music/DuckTales Music (NES) - The Moon Theme.wav"
gamestartmusic="C:/Users/caleb_000/Documents/Python/Python Game/Music/Skyrim Theme 8-Bit.wav"
