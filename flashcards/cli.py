#!/usr/bin/env python3
import os
import sys

BASEDIR = os.path.dirname(os.path.abspath(__file__))
FOLDER = os.path.join(BASEDIR, "flashcardsfolder")


def help():
    print("""Commands:
    i - initialise the flashcard folder
    vs - view all sets created
    ms - makes a set of flashcards
    rm - removes specified set
    os - opens sepecific set to practice""")


def initflashcardfolder():
    print("Initialising flashcards...")
    try:
        os.mkdir(FOLDER)
        print("Initialised sucessfully")
    except Exception:
        print("flashcards is already initialised, youre all ready to memorise")


def viewsets():
    if not os.path.exists(FOLDER):
        print("Flashcard folder isnt initialised, run: flashcards init")
    if len(os.listdir(FOLDER)) == 0:
        print("You have no flashcard sets or folders, make one with either ms or mf")
    for i in os.listdir(FOLDER):
        print(i.removesuffix(".txt"))


def makeset():
    name = input("What do you want to name the set: ")
    name = name.replace(" ", "_")
    if "/" in name:
        while "/" in name:
            name = input(
                "The last name you selecetd was invalid because you used forbidden characters"
            )
    path = os.path.join(FOLDER, f"{name}.txt")
    with open(path, "w+") as f:
        print(
            f"Creating flashcards in {name} \nto stop adding flashcards, press `Enter`"
        )
        while True:
            term = input("enter a term: ")
            if term == "":
                break
            definition = input("enter a definition: ")
            f.write(f"{term},{definition}\n")
            print(f"added {term} : {definition}")


def makefolder():
    foldername = input("What do you want to name your folder: ")
    os.mkdir(os.path.join(FOLDER, foldername))
    print(foldername, "made at ", os.path.join(FOLDER, foldername))


def removeset():
    settoremove = input("What set would you like to remove: ")
    settoremove = settoremove + ".txt"
    for i in os.listdir(FOLDER):
        if i == settoremove:
            removefileconfirmation = input(
                f"Are you sure you want to delete {i}? [y/n]: "
            )
            if removefileconfirmation[0] == "y":
                os.remove(os.path.join(FOLDER, i))
                print(i, "removed")


def openset():
    settoopen = input("What set would you like to open: ")
    pathofset = os.path.join(FOLDER, f"{settoopen}.txt")
    try:
        with open(pathofset, "r") as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                line.removesuffix("\n")
                parts = line.split(",")
                term = parts[0]
                definition = parts[1]

                question = input(f"What is the definition of {term}? ")
                if question.strip().lower() == definition.lower():
                    print("Well done! thats correct")
                else:
                    print(f"You might have made a typo, the answer is {definition}")

    except:
        print("The set you want to see dosent exist")


def main():
    if len(sys.argv) > 3:
        print("To see list of commands, type `flashcards h` ")
        sys.exit()

    command = sys.argv[1]

    commands = {
        "h": help,
        "i": initflashcardfolder,
        "vs": viewsets,
        "ms": makeset,
        "rm": removeset,
        "os": openset,
    }
    if command in commands:
        if command != "i" and not os.path.exists(FOLDER):
            print(
                "You dont have the flashcards folder initialised, you should run `flashcards i` to initialise it."
            )
        commands[command]()
    else:
        print(
            f"{command} is invalid, to see full list of commands type `flashcards h`."
        )
