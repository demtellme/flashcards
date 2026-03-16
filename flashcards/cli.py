#!/usr/bin/env python3
import os
import random
import shutil
import sys

BASEDIR = os.path.dirname(__file__)
BASEFOLDER = os.path.join(BASEDIR, ".flashcardsfolder")

pid = os.getppid()

if os.path.exists("/tmp/fcards_state"):
    with open("/tmp/fcards_state") as f:
        lines = f.readlines()
        currentfolder = lines[0].strip()
        if len(lines) > 1:
            oldpid = int(lines[1])
            if oldpid != pid:
                currentfolder = BASEFOLDER
else:
    currentfolder = BASEFOLDER


def help():
    print("""Commands:
    v <folder> - view all items created in a folder, if <folder> isnt specified it will show items in the base directory
    ms <n> <folder> - makes a set of flashcards, if folder is specified it will add the set to the folder, if the folder dosent exist it will make it
    rm <n> - removes specified item
    ls <n> <folder> - open a set to learn, you get asked to define the terms in your flashcards, if folder not specified it defalts to default directory
    os <n> <folder> - opens sepecific set to practice, just normal flipping of flashcards
    cf - displays the current working folder
    u <setname> - update a flashcard set, you can remove terms, add terms, update terms or definitions
    f <folder> - sets working folder to specified folder, to return to the original folder, just call `fcards f` with no additional arguments
    """)

def viewsets(folder=None):
    if not folder:
        folder = currentfolder
    elif not os.path.exists(folder):
        print("Flashcard folder isnt initialised, run: flashcards init")
    elif len(os.listdir(folder)) == 0:
        print(
            "You have no flashcard sets in this folder, make one with either ms or mf"
        )
    for i in os.listdir(folder):
        fullpath = os.path.join(folder, i)
        if os.path.isfile(fullpath):
            print("set - ", i.removesuffix(".txt"))
        else:
            print("folder - ", i)


def makeset(setname, folder=None):
    setname = setname.replace(" ", "_")
    if "/" in setname:
        while "/" in setname:
            setname = input(
                "The last name you selecetd was invalid because you used forbidden characters"
            )
    if folder:
        folder = os.path.join(currentfolder, folder)
        if not os.path.isdir(folder):
            os.mkdir(folder)
            print(f"Made {folder} folder, didnt exist previously")
            os.chdir(folder)
    else:
        folder = currentfolder

    path = os.path.join(folder, f"{setname}.txt")

    print(f"Creating {setname} in {folder} \nto stop adding flashcards, press `Enter`")
    while True:
        term = input("enter a term: ")
        if term == "":
            break
        definition = input("enter a definition: ")
        term = term.replace(":", "-")
        definition = definition.replace(":", "-")
        open(path, "a+").write(f"{term}:{definition}\n")
        print(f"added {term} : {definition}")


def makefolder(foldername):
    os.mkdir(os.path.join(currentfolder, foldername))
    print(foldername, "made at ", os.path.join(currentfolder, foldername))


def remove(itemtoremove):
    itemtoremove = itemtoremove.replace(" ", "_")
    for i in os.listdir(currentfolder):
        i = i.removesuffix(".txt")
        if i.lower() == itemtoremove.lower():
            removefileconfirmation = input(
                f"Are you sure you want to delete {i}? [y/n]: "
            )
            if removefileconfirmation.lower() == "y":
                path = os.path.join(currentfolder, i)
                if os.path.isfile(path):
                    os.remove(path + ".txt")
                    print(i, "removed")
                elif os.path.isdir(path):
                    shutil.rmtree(path)
                    print(i, "removed")


def learnset(settolearn, folder=None):
    if not folder:
        folder = currentfolder
    else:
        folder = os.path.join(currentfolder, folder)
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

    except Exception as err:
        print("The set you want to see dosent exist", err)


def openset(setname, folder=None):
    try:
        if not folder:
            folderpath = currentfolder
        else:
            folderpath = os.path.join(currentfolder, folder)

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
    print("you are currently working in ", currentfolder)


def updateset(setname, folder=None):
    if not folder:
        folderpath = currentfolder
    else:
        folderpath = os.path.join(currentfolder, folder)

    setpath = os.path.join(folderpath, setname + ".txt")
    try:
        lines = open(setpath).readlines()
        options = ["a", "rm", "rp", "e"]
        for i, line in enumerate(lines):
            print(i, "-", line.strip())
        print(
            "Your options are:\n    add a line - a\n    remove a line - rm\n    replace a line - rp\n   edit line - e"
        )
        choice = input()
        if choice.lower() not in options:
            print("Please select a valid option")
        else:
            if choice == "a":
                print(
                    f"Adding terms to {setname} \nto stop adding flashcards, press `Enter`"
                )
                while True:
                    term = input("enter a term: ")
                    if term == "":
                        break
                    definition = input("enter a definition: ")
                    term = term.replace(":", "-")
                    definition = definition.replace(":", "-")
                    open(setpath, "a+").write(f"{term}:{definition}\n")
                    print(f"added {term} : {definition}")
            elif choice == "rm":
                num = int(input("enter the number of the line youd like to remove: "))
                del lines[num]
                open(setpath, "w").writelines(lines)
                print(f"Removed line {num}")
            elif choice == "rp":
                num = int(
                    input(
                        "enter the number of the line youd like to replace - to keep something the same press `Enter`: "
                    )
                )
                parts = lines[num].split(":")
                term = parts[0]
                definition = parts[1]

                choice = input("What would you like to replace the term with: ")
                if choice != "":
                    term = choice
                choice = input("What would you like to replace the definition with: ")
                if choice != "":
                    definition = choice
                lines[num] = f"{term}:{definition}\n"
                open(setpath, "w").writelines(lines)

            else:
                num = int(input("enter the number of the line youd like to edit: "))
                parts = lines[num].split(":")
                term = parts[0]
                definition = parts[1].strip()
                print(f"current: {term} : {definition}")
                new_term = input(f"new term (press Enter to keep '{term}'): ")
                new_definition = input(
                    f"new definition (press Enter to keep '{definition}'): "
                )
                if new_term != "":
                    term = new_term
                if new_definition != "":
                    definition = new_definition
                lines[num] = f"{term}:{definition}\n"
                open(setpath, "w").writelines(lines)
                print(f"Updated line {num}")
    except Exception as err:
        print("No such file exists", err)


def changefolder(foldertogointo=None):
    global currentfolder
    if not foldertogointo:
        currentfolder = BASEFOLDER
        os.chdir(BASEDIR)
    else:
        os.chdir(os.path.join(currentfolder, foldertogointo))
        currentfolder = os.path.join(currentfolder, foldertogointo)

    open("/tmp/fcards_state", "w").write(f"{currentfolder}\n{pid}")


def main():
    if os.path.exists(currentfolder):
        os.chdir(currentfolder)

    if len(sys.argv) > 4:
        print(
            "To see list of commands, type `flashcards h`, you gave too many arguments"
        )
        sys.exit()

    if len(sys.argv) < 2:
        print("No command given. Type `fcards h` for help.")
        return

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
        "v": viewsets,
        "ms": makeset,
        "rm": remove,
        "ls": learnset,
        "os": openset,
        "cf": showcurrentfolder,
        "mf": makefolder,
        "u": updateset,
        "f": changefolder,
    }
    if command in commands:
        if argument1 and not argument2:
            commands[command](argument1)
        elif argument1 and argument2:
            commands[command](argument1, argument2)
        else:
            commands[command]()
    else:
        print(
            f"{command} is invalid, to see full list of commands type `flashcards h`."
        )
