#!/usr/bin/env python3
import os, sys

def h():
    print('Commands: \n initflashcards - initialise the flashcard folder \ nviewsets - view all sets created \n makeset - makes a set of flashcards \n makefolder - makes a folder to contain flashcards, can be used for subjects/topics \nremoveset - removes specified set \n openset - opens sepecific set to practice')

def initflashcards():
    pass
def viewsets():
    pass
def makeset():
    pass
def makefolder():
    pass
def removeset():
    pass
def openset():
    pass

if len(sys.argv) > 2:
    print('To see list of commands, type flashcards h ')
    sys.exit()

command = sys.argv[1]

commands = {
    'h':h,
    'initflashcards':initflashcards,
    'viewsets':viewsets,
    'makeset':makeset,
    'makefolder':makefolder,
    'removeset':removeset,
    'openset':openset
}
if command in commands:
    commands[command]()
else:
    print(f'{command} is invalid, to see full list of commands type flashcards h')