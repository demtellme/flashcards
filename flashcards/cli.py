#!/usr/bin/env python3
import os
import sys

FOLDER = "flashcardsfolder"


def help():
    print("""Commands:
    initflashcards - initialise the flashcard folder
    viewsets - view all sets created
    makeset - makes a set of flashcards
    makefolder - makes a folder to contain flashcards, can be used for subjects/topics
    removeset - removes specified set
    openset - opens sepecific set to practice""")


def initflashcardfolder():
    print("Initialising flashcards...")
    try:
        os.mkdir(FOLDER)
        print("Initialised sucessfully")
    except:
        print("flashcards is already initialised, youre all ready to memorise")


def viewsets():
    if not os.path.isfile(FOLDER):
        print("Flashcard folder isnt initialised, run: flashcards init")
    if len(os.listdir(FOLDER)) == 0:
        print("You have no flashcard sets or folders, make one with either ms or mf")
    for i in os.listdir("flashcardsfolder"):
        print(i)


def makeset():
    pass


def makefolder():
    pass


def removeset():
    pass


def openset():
    pass


def main():
    if len(sys.argv) > 2:
        print("To see list of commands, type flashcards h ")
        sys.exit()

    command = sys.argv[1]

    commands = {
        "h": help,
        "i": initflashcardfolder,
        "view": viewsets,
        "ms": makeset,
        "mf": makefolder,
        "rs": removeset,
        "os": openset,
    }
    if command in commands:
        commands[command]()
    else:
        print(f"{command} is invalid, to see full list of commands type flashcards h")
