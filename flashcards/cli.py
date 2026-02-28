#!/usr/bin/env python3
import os
import random
import shutil
import sys

BASEDIR = os.path.dirname(os.path.abspath(__file__))
FOLDER = os.path.join(BASEDIR, "flashcardsfolder")


def help():
    print("""Commands:
    i - initialise the flashcard folder
    v <folder> - view all items created in a folder, if <folder> isnt specified it will show items in the base directory
    ms <name> <folder> - makes a set of flashcards, if folder is specified it will add the set to the folder, if the folder dosent exist it will make it
    rm <name> - removes specified item
    ls <name> <folder> - open a set to learn, you get asked to define the terms in your flashcards, if folder not specified it defalts to default directory
    os <name> <folder> - opens sepecific set to practice, just normal flipping of flashcards
    cf - displays the current working folder


    """)


def initflashcardfolder():
    print("Initialising flashcards...")
    try:
        os.mkdir(FOLDER)
        print("Initialised sucessfully")
    except Exception:
        print("flashcards is already initialised, youre all ready to memorise")


def viewsets(folder=None):
    if not folder:
        folder = FOLDER
    elif not os.path.exists(FOLDER):
        print("Flashcard folder isnt initialised, run: flashcards init")
    elif len(os.listdir(folder)) == 0:
        print(
            "You have no flashcard sets in this folder, make one with either ms or mf"
        )
    for i in os.listdir(folder):
        print(i.removesuffix(".txt"))


def makeset(setname, folder=None):
    setname = setname.replace(" ", "_")
    if "/" in setname:
        while "/" in setname:
            setname = input(
                "The last name you selecetd was invalid because you used forbidden characters"
            )
    if folder:
        folder = os.path.join(FOLDER, folder)
        if not os.path.isdir(folder):
            os.mkdir(folder)
            print(f"Made {folder} folder, didnt exist previously")
            os.chdir(folder)
    else:
        folder = FOLDER

    path = os.path.join(folder, f"{setname}.txt")
    with open(path, "w+") as f:
        print(
            f"Creating {setname} in {folder} \nto stop adding flashcards, press `Enter`"
        )
        while True:
            term = input("enter a term: ")
            if term == "":
                break
            definition = input("enter a definition: ")
            f.write(f"{term}:{definition}\n")
            print(f"added {term} : {definition}")


def makefolder(foldername):
    os.mkdir(os.path.join(FOLDER, foldername))
    print(foldername, "made at ", os.path.join(FOLDER, foldername))


def remove(itemtoremove):
    itemtoremove = itemtoremove.replace(" ", "_")
    for i in os.listdir(FOLDER):
        i = i.removesuffix(".txt")
        if i.lower() == itemtoremove.lower():
            removefileconfirmation = input(
                f"Are you sure you want to delete {i}? [y/n]: "
            )
            if removefileconfirmation.lower() == "y":
                path = os.path.join(FOLDER, i)
                if os.path.isfile(path):
                    os.remove(path + ".txt")
                    print(i, "removed")
                elif os.path.isdir(path):
                    shutil.rmtree(path)
                    print(i, "removed")


def learnset(settolearn, folder=None):
    if not folder:
        folder = FOLDER
    else:
        folder = os.path.join(FOLDER, folder)
    settolearn = settolearn.replace(" ", "_")
    pathofset = os.path.join(folder, f"{settolearn}.txt")
    try:
        with open(pathofset, "r") as f:
            lines = f.readlines()
            random.shuffle(lines)
            for line in lines:
                line = line.strip()
                parts = line.split(":")
                term = parts[0]
                definition = parts[1]

                question = input(f"What is the definition of {term}? ")
                if question.strip().lower() == definition.lower():
                    print("Well done! thats correct")
                else:
                    print(f"You might have made a typo, the answer is {definition}")

    except Exception:
        print("The set you want to see dosent exist")


def openset(setname, folder=None):
    try:
        if not folder:
            folderpath = FOLDER
        else:
            folderpath = os.path.join(FOLDER, folder)

        print("Press Enter to see definition, e to exit")
        with open(os.path.join(folderpath, setname + ".txt"), "r") as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                parts = line.split(":")

                term = parts[0]
                definition = parts[1]

                print(term)
                choice = input()
                print(definition)
                choice = input()
                if choice.lower() == "e":
                    break

    except Exception as er:
        print(f"no file '{setname}' found", er)


def showcurrentfolder():
    print("you are currently working in ", os.getcwd())


def main():
    os.chdir(FOLDER)
    if len(sys.argv) > 4:
        print(
            "To see list of commands, type `flashcards h`, you gave too many arguments"
        )
        sys.exit()

    command = sys.argv[1]
    argument1 = None
    argument2 = None
    if len(sys.argv) == 3:
        argument1 = sys.argv[2]
    elif len(sys.argv) == 4:
        argument1 = sys.argv[2]
        argument2 = sys.argv[3]

    commands = {
        "h": help,
        "i": initflashcardfolder,
        "v": viewsets,
        "ms": makeset,
        "rm": remove,
        "ls": learnset,
        "os": openset,
        "cf": showcurrentfolder,
        "mf": makefolder,
    }
    if command in commands:
        if command != "i" and not os.path.exists(FOLDER):
            print(
                "You dont have the flashcards folder initialised, you should run `flashcards i` to initialise it."
            )
        elif argument1 and not argument2:
            commands[command](argument1)
        elif argument1 and argument2:
            commands[command](argument1, argument2)
        else:
            commands[command]()
    else:
        print(
            f"{command} is invalid, to see full list of commands type `flashcards h`."
        )
